from django.urls import path
from . import views



urlpatterns = [
    path('categories/', views.blog, name="blog"),
    path('single-post/<uuid:post_id>/', views.singlePost, name="single-post"),
]
