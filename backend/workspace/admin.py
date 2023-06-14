from django.contrib import admin
from .models import WorkSpace, Column, Task


class WorkSpaceAdmin(admin.ModelAdmin):
    fields = ('title',)


class ColumnAdmin(admin.ModelAdmin):
    fields = ('title',)


class TaskAdmin(admin.ModelAdmin):
    fields = ('title',)


admin.site.register(WorkSpace, WorkSpaceAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Task, TaskAdmin)
