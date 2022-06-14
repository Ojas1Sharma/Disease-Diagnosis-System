from django.urls import path
from . import views

urlpatterns = [
    path('heart', views.heart, name="heart"),
    path('kidney', views.diabetes, name="diabetes"),
    path('liver', views.breast, name="breast"),
    path('', views.heart, name="home"),
]
