from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import Post
from django.http import HttpResponse
import operator
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def contrib(request, pk):
    post_to_mutate = Post.objects.get(pk=pk)
    amt = request.GET.get('q')
    try:
        amt= int(amt)

    except ValueError:
        amt = None

    count = post_to_mutate.amt_raised
    count = count + amt
    Post.objects.filter(pk=pk).update(amt_raised=count)
    post_again = Post.objects.get(pk=pk)
    if post_again.amt_raised >= post_again.amt_sought:
        Post.objects.filter(pk=pk).update(post_status="Successfully funded")

    return render(request,'blog/success_contrib.html')


def search(request):
    template = 'blog/home.html'
    query = request.GET.get('q')
    results = Post.objects.filter(Q(title__icontains=query) | Q(
        content__icontains=query) | Q(category__icontains=query)| Q(author__username__icontains=query))

    context = {'posts': results}

    return render(request, template, context)

def success(request):
    template = 'blog/home.html'
    results = Post.objects.filter(post_status = "Successfully funded")

    context = {'posts': results}

    return render(request, template, context)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'category', 'amt_sought']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'category', 'amt_sought']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
