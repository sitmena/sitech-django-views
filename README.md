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
    from example.Blog.models import Post
    from sitech_views import UpdateView, DeleteView

    class UpdatePost(UpdateView):
        model = Post
        fields = ['title', 'content']
        template_name = 'update_post.html'
	
	def before_get_object(self):
            pass #called befor get object from db 

	def after_get_object(self):
            pass #called after get object from db 


    class DeletePost(DeleteView):
        model = Post
        success_url = reverse_lazy('posts-list')
	
	def before_get_object(self):
            pass #called befor get object from db 

	def after_get_object(self):
            pass #called after get object from db 
```
