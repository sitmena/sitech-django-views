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
    from sitech_views import FormView, CreateView, UpdateView, DeleteView

    
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
