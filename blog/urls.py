from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.list, name="index"),
    path('post/<int:id>/', views.viewPost, name='post'),
    path('profile', views.loadProfile, name='profile'),
]