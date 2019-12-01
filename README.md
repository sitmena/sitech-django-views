# Sitech Django Views
	
	
	-- Sitech Views ---+---- Base ----------+-- 1) View
			   |                    |
			   | 			+-- 2) RedirectView  
			   | 		        |	                              
			   | 			+-- 3) TemplateView      
			   | 
			   |
			   +--- Detail ---------+-- 4) DetailView
			   |	
			   |
			   +---  List ----------+-- 5) ListView    
			   |	
			   |
			   +---- Edit ----------+-- 6) CreateView
					        |
					        +-- 7) UpdateView  
					        |	                              
					        +-- 8) DeleteView
					        |
					        +-- 9) FormView    
					    

## Installation

Run the [pip](https://pip.pypa.io/en/stable/) command to install the latest version:

```bash
   pip install git+https://github.com/sitmena/sitech-django-views.git@v1.0
```

## Usage

Import and use the views.

    from sitech_views import ListView, DetailView


For example:

```python
    from example.Blog.forms import SampleForm
    from example.Blog.models import Post
    from sitech_views import RedirectView, TemplateView, DetailView, CreateView, UpdateView, DeleteView, FormView

    #RedirectView
    class PostCounterRedirectView(RedirectView):
        permanent = False
        query_string = True
        pattern_name = 'post-detail'

        def get_redirect_url(self, *args, **kwargs):
            post = get_object_or_404(Post, pk=kwargs['pk'])
            post.update_counter()
            return super().get_redirect_url(*args, **kwargs)


    #TemplateView	
    class HomePageView(TemplateView):
        template_name = "home.html"
	
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['latest_posts'] = Post.objects.all()[:5]
            return context
	    
	    
    #DetailView
    class PostDetail(DetailView):
        model = Post
        template_name = 'update_detail.html'
	
	def before_get_object(self):
            pass #called befor get object from db 

	def after_get_object(self):
            pass #called after get object from db 


    #CreateView
    class CreatePost(CreateView):
        model = Post
        fields = ['title', 'content']
	template_name = 'create_post.html'
	success_url = reverse_lazy('postsList')


    #UpdateView
    class UpdatePost(UpdateView):
        model = Post
        fields = ['title', 'content']
        template_name = 'update_post.html'
	
	def before_get_object(self):
            pass #called befor get object from db 

	def after_get_object(self):
            pass #called after get object from db 


    #DeleteView
    class DeletePost(DeleteView):
        model = Post
        success_url = reverse_lazy('postsList')
	
	def before_get_object(self):
            pass #called befor get object from db 

	def after_get_object(self):
            pass #called after get object from db 
	    
	    
    #FormView	    
    class SampleFormView(FormView):
        template_name = 'sample_form.html'
        form_class = SampleForm
        success_url = reverse_lazy('successUrl')

        def form_valid(self, form):
            # This method is called when valid form data has been POSTed.
            # It should return an HttpResponse.
            return super().form_valid(form) 	    
```
