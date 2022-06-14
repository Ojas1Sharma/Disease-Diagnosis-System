from django.urls import path
from . import views
# from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView


urlpatterns = [
#    path('register/',views.register_request, name='blog-about'),
       path("", views.home, name="home")
]