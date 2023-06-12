from django.db import models


class WorkSpace(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Название пространства')
    discription = models.TextField(
        blank=True, verbose_name='Описание пространства')
    column = ...  # Колонки со статусом
    users = ...  # Пользователи которые участвуют в раб.пространстве

    class Meta:
        verbose_name = 'Рабочее пространсво'
        verbose_name_plural = 'Рабочии пространсва'

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Название пространства')
    discription = models.TextField(
        blank=True, verbose_name='Описание пространства')
    deadline = models.DateField(
        blank=True, verbose_name='Срок выполнения')
    comment = ...  # Комментарии к задачам
    attachments = ...  # Вложеные файлы, картинки и тд.

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title


# Колонки, с статусом задачи - В работе, принято, не принято и тд.
class Column(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Название пространства')
    task = ...  # Здесь будут хранится задачи

    class Meta:
        verbose_name = 'Колонка'
        verbose_name_plural = 'Колонки'

    def __str__(self):
        return self.title


# Роль для пользователей в пространстве, что они могут делать
class UserRole(models.Model):
    pass
