from django.urls import path
from .views import BlogDetail, BlogIndex, CreateBlog

urlpatterns = [
    path('blog/<int:pk>', BlogDetail.as_view(), name='blog-detail'),
    path('blogs', BlogIndex.as_view(), name='blogs'),
    path('blog/create', CreateBlog.as_view(), name='blog-create'),
]
