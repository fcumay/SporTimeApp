from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.


class Post(models.Model):
    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'

    title = models.CharField(max_length=200, help_text='Не более 200 символов', db_index=True)
    # content = models.TextField(max_length=5000, blank=True, null=True, help_text='Не более 5000 символов')
    content = RichTextField(blank=True, null=True, help_text='Не более 5000 символов',max_length=5000)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)
    likes = models.ManyToManyField(User, related_name='postcomment', blank=True)
    reply = models.ForeignKey('self', null=True, related_name='reply_ok', on_delete=models.CASCADE)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Trainer(models.Model):
    class Meta:
        verbose_name = 'Добавить тренера'
        verbose_name_plural = 'Тренеры'
    name =  models.CharField(max_length=200, help_text='Не более 200 символов', db_index=True)
    info = RichTextField(blank=True, null=True, help_text='Не более 5000 символов',max_length=5000)
    image = models.ImageField(upload_to='trainer/', blank=True, null=True)
    image_left = 132

    def __str__(self):
        return self.name

    def add_image_left(self):
        if Trainer.image_left==1272:
            Trainer.image_left=132
        Trainer.image_left +=285
        return Trainer.image_left

    def get_absolute_url(self):
        return reverse('trainer', kwargs={'trainer_id': self.pk})
