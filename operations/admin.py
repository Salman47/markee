from django.contrib import admin
from operations.models import Task, ToDoItem


class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'task_number', 'client_name', 'quantity',
        'start_date', 'due_date', 'approval_status'
    ]


class ToDoItemAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'status', 'description'
    ]


admin.site.register(Task, TaskAdmin)
admin.site.register(ToDoItem, ToDoItemAdmin)
