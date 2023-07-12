from django.contrib import admin

from .models import Board, Column, Task, Comment


class BoardAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'title', 'is_public')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    readonly_fields = ('created_at',)
    fields = ('title', 'description', 'is_public', 'columns', 'created_at')


class ColumnAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    fields = ('title', 'task')


class TaskAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    fields = ('title', 'description', 'comments')


class CommentAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id',)
    list_display_links = ('id',)
    readonly_fields = ('created_at',)
    fields = ('text', 'created_at')


admin.site.register(Board, BoardAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
