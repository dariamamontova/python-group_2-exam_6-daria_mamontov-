from django.views.generic import DetailView, CreateView, UpdateView, View, ListView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from webapp.forms import PostForm, UserForm
from webapp.models import User, Post, UserInfo
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return Post.objects.order_by('date')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'

    def get_success_url(self):
        return reverse('webapp:post_list')

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = UserInfo
    template_name = 'user_update.html'
    form_class = UserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.userinfo = UserInfo.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:user_detail', kwargs={'pk': self.object.pk})