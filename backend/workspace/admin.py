from django.contrib import admin
from .models import WorkSpace, Column, Task


class WorkSpaceAdmin(admin.ModelAdmin):
    fields = ('title', 'discription', 'column')
    readonly_fields = ('create_at',)
    list_display = ('title', 'create_at')


class ColumnAdmin(admin.ModelAdmin):
    fields = ('title', 'task')
    list_display = ('title',)


class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'discription', 'deadline')
    list_display = ('title', 'deadline')


admin.site.register(WorkSpace, WorkSpaceAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Task, TaskAdmin)
