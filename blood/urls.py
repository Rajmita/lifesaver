from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.create_post, name='create_post'),
    path('about/', views.about, name='about'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
    path('help/', views.help_page, name='help_page'),
]


