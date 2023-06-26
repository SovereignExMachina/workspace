from django.db import models
from django.urls import reverse


class WorkSpace(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Название пространства')
    discription = models.TextField(
        blank=True, verbose_name='Описание пространства')
    # Колонки со статусом
    column = models.ManyToManyField(
        'Column', blank=True, verbose_name='Колонка', related_name='columns')
    create_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    # users = ...  # Пользователи которые участвуют в раб.пространстве

    def get_absolute_url(self):
        return reverse("workspace:ws_detail", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name = 'Рабочее пространсво'
        verbose_name_plural = 'Рабочии пространсва'
        ordering = ['-create_at']

    def __str__(self):
        return self.title


# Колонки, с статусом задачи - В работе, принято, не принято и тд.
class Column(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Имя колонки')
    # Здесь будут хранится задачи
    task = models.ManyToManyField(
        'Task', blank=True, verbose_name='Задачи', related_name='tasks')

    class Meta:
        verbose_name = 'Колонка'
        verbose_name_plural = 'Колонки'
        ordering = ['-title']

    def __str__(self):
        return self.title


""" class Comment(models.Model):
    author = ... # Автор комментария
    message = models.TextField(verbose_name='Текст коментария')
    date_at = ... # Дата комментария

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии' """


class Task(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Имя задачи')
    discription = models.TextField(
        blank=True, verbose_name='Описание задачи')
    deadline = models.DateField(
        blank=True, verbose_name='Срок выполнения')
    # comment = ...  # Комментарии к задачам
    # attachments = ...  # Вложеные файлы, картинки и тд.

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title


# Роль для пользователей в пространстве, что они могут делать
class UserRole(models.Model):
    pass
