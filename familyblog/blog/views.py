from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from blog.models import Post, Category
from . forms import PostForm, EditForm


class PostView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-date_created']
    paginate_by = 5  

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostView, self). get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostDetailView(DetailView):
    # login_url = '/'
    # redirect_field_name = 'home'
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self). get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        # context = super(PostDetailView, self).category_renderer(*args, **kwargs)
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class AddCategoryView(CreateView):
    model = Category    
    template_name = 'blog/add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('add_category')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self). get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' ')).order_by('-date_created')
    paginator = Paginator(category_posts, 5) 
    page_number = request.GET.get('page')
    # nums = "a" * paginator.num_pages
    nums = paginator.num_pages
    category_posts = paginator.get_page(page_number)
    return render(request, 'blog/categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts, 'nums':nums})

def AuthorView(request, author):
    author_posts = Post.objects.filter(author=author).order_by('-date_created')
    author_name = User.objects.get(id=author)
    paginator = Paginator(author_posts, 5) 
    page_number = request.GET.get('page')
    nums = "a" * paginator.num_pages
    author_posts = paginator.get_page(page_number)
    return render(request, 'blog/author.html', {'author':author_name, 'author_posts':author_posts, 'nums':nums})


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'
    
    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog_home')
