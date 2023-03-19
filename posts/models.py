from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(
        max_length=100, 
        blank=False, 
        verbose_name='заголовок',
    )
    body = models.TextField(
        blank=False, 
        verbose_name='поле текста',
    )
    date = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
