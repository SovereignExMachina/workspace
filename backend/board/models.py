from django.db import models
from django.urls import reverse


class Board(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    #user = 
    #users =
    is_public = models.BooleanField(default=False, verbose_name='Открытая/Закрытая')
    columns = models.ManyToManyField('Column', related_name='boards', blank=True, verbose_name='Колонки')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('board:board_detail', kwargs={'pk': self.pk})
    


class Column(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    task = models.ManyToManyField('Task', related_name='columns', blank=True, verbose_name='Задачи')

    class Meta:
        verbose_name = 'Колонка'
        verbose_name_plural = 'Колонки'

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    #attachment = models.FileField()
    comments = models.ManyToManyField('Comment', related_name='tasks', blank=True, verbose_name='Коментарии')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(blank=True, verbose_name='Текст')
    #author = 
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
