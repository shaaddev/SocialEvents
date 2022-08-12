
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('user/<str:username>/', views.UserPostList.as_view(), name='user_post'),
    path('create/new/', views.CreatePostView.as_view(template_name='posts/create_post.html'), name='create'),
    path('update/<pk>/', views.UpdatePostView.as_view(template_name='posts/update_post.html'), name='update'),
    path('remove/<pk>/', views.DeletePostView.as_view(template_name='posts/delete_post.html'), name='delete'),
    path('category/', views.CategoryPostView.as_view(), name="category"),
    path('add_category/', views.AddCategory.as_view(), name="add_category"),
    path('update_category/<pk>/', views.EditCategory.as_view(), name="edit_category"),
    path('remove_category/<pk>/', views.RemoveCategory.as_view(), name="remove_category"),
    path('category_posts/<str:cats>/', views.categoryposts, name="view_category"),
]