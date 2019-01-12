from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from webapp.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserListView, \
    UserDetailView, UserUpdateView


app_name = 'webapp'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/create', PostCreateView.as_view(), name='add_post'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('users', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('user/update/<int:pk>', UserUpdateView.as_view(), name='user_update')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)