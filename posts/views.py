from curses.ascii import HT
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from .models import Post, Category
from .forms import PostForm, CategoryForm

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class PostList(ListView):
    model = Post

class UserPostList(ListView):
    model = Post
    template_name = 'posts/user_posts.html'

class CategoryPostView(ListView):
    model = Category
    template_name = 'posts/category.html'

class AddCategory(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'posts/add_category.html'
    success_url = reverse_lazy('posts:category')

class EditCategory(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'posts/edit_category.html'
    success_url = reverse_lazy('posts:category')

class RemoveCategory(DeleteView):
    model = Category
    template_name = 'posts/remove_category.html'
    success_url = reverse_lazy('posts:category')

def categoryposts(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ''))
    return render(request, 'posts/view_category_posts.html', {'cats': cats, 'category_posts': category_posts} )


class CreatePostView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('posts:home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('posts:home')


class DeletePostView(LoginRequiredMixin, DeleteView):
    
    model = Post
    success_url = reverse_lazy('posts:home')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)