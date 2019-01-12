from django.views.generic import DetailView, CreateView, UpdateView, View, ListView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from webapp.forms import PostForm
from webapp.models import User, Post

from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetailView(DeleteView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})