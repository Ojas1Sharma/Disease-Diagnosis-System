from django.urls import path
from . import views
# from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView


urlpatterns = [
   path('register/',views.register_request, name='blog-about'),
       path("login/", views.login_request, name="login"),
       path("", views.login_request, name="login")
]