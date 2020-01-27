from django.views.generic import ListView as DjangoListView, View as DjangoView
from django.views.generic.edit import FormMixin
from django.http import Http404
from django.http import JsonResponse

class ListView(DjangoListView, FormMixin):
    """
    Render some list of objects, set by `self.model` or `self.queryset`.
    `self.queryset` can actually be any iterable of items, not just a queryset.
    """
    paginate_by_kwarg = 'per-page'
    paginate_by_limit = None
    default_paginate_by = None
    
    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""
        form = None
        if form_class is None:
            form_class = self.get_form_class()
        if form_class is not None:
            form = form_class(**self.get_form_kwargs())
        return form

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
        }

        kwargs.update({
            'data': self.request.GET,
        })
        return kwargs

    def get_paginate_by(self, queryset):
        if not self.paginate_by:
            if not self.paginate_by_limit:
                paginate_by = self.default_paginate_by
            else:
                paginate_by_kwarg = self.paginate_by_kwarg
                paginate_by = self.kwargs.get(paginate_by_kwarg) or self.request.GET.get(paginate_by_kwarg) or self.default_paginate_by

            self.set_paginate_by(paginate_by)
        return self.paginate_by

    def set_paginate_by(self, value):
        if value:
            value = int(value)
            if isinstance(self.paginate_by_limit, list) and len(self.paginate_by_limit) == 2:
                if value < self.paginate_by_limit[0]:
                    value = self.paginate_by_limit[0]
                elif value > self.paginate_by_limit[1]:
                    value = self.paginate_by_limit[1]
        self.paginate_by = value
    
    def paginate_queryset(self, queryset, page_size):
        """Paginate the queryset, if needed."""
        paginator = self.get_paginator(
            queryset, page_size, orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty())
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404(_("Page is not 'last', nor can it be converted to an int."))
        page_number = page_number if page_number <= paginator.num_pages else paginator.num_pages        
        try:
            page = paginator.page(page_number)
            return (paginator, page, page.object_list, page.has_other_pages())
        except InvalidPage as e:
            raise Http404(_('Invalid page (%(page_number)s): %(message)s') % {
                'page_number': page_number,
                'message': str(e)
            })    
            
                  
class BulkActionView(DjangoView):
    """
    BulkActionView
    """
    def get(self, request, action, *args, **kwargs):
        if hasattr(self, '_' + action):
            return self.http_method_not_allowed(request, *args, **kwargs)
        else:
            raise Http404(_("Page not found"))

    def post(self, request, action, *args, **kwargs):
        if hasattr(self, '_' + action):
            pks = request.POST.getlist('pks[]')
            if pks:
                action_function = getattr(self, '_' + action)
                action_function(pks)
            return JsonResponse({'success': True})
        else:
            raise Http404(_("Page not found"))

