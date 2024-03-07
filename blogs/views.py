from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Category, Post, Comment
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class BlogForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'body', 'category', 'cover_image']


class BlogIndex(ListView):
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'components/blogs.html'
    context_object_name = 'posts'


class BlogDetail(DetailView):
    model = Post
    template_name = 'components/blog-detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post = super().get_object()
        return get_object_or_404(Post, pk=post.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        return context


@method_decorator(login_required, name='dispatch')
class CreateBlog(CreateView):
    model = Post
    template_name = 'components/blog-create.html'
    form_class = BlogForm
    context_object_name = 'blog'
    success_url = reverse_lazy('blogs')

    def form_valid(self, form):
        form.instance.author = self.request.user
        category_name = form.cleaned_data.get('category')
        category = get_object_or_404(Category, name=category_name)
        form.instance.category = category
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogForm()  # add form instance to context
        return context
