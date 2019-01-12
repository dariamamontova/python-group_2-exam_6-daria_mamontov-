from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from webapp.views import PostListView, PostDetailView, PostCreateView


app_name = 'webapp'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/create', PostCreateView.as_view(), name='add_post')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)