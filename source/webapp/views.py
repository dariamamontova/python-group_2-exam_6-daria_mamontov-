from django.views.generic import DetailView, CreateView, UpdateView, View, ListView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from webapp.models import User, Post

from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetailView(DeleteView):
    model = Post
    template_name = 'post_detail.html'