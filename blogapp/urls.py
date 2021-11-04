from django.urls import path
from . import views

app_name = "blogapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('post/details/<slug>/<int:pk>', views.blogpost, name='blogpost')
]