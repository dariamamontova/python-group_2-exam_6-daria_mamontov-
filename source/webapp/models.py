from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user_info', verbose_name='Пользователь')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    picture = models.ImageField(verbose_name='Фотография')
    friend = models.ManyToManyField('UserInfo', blank=True, related_name='user_friend', verbose_name='Друг')

    def __str__(self):
        return self.user.get_full_name()

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(UserInfo, on_delete=models.PROTECT, related_name='post_author', verbose_name='Автор')

    def __str__(self):
        return self.title
