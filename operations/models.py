from django.db import models
from account.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_number = models.CharField(max_length=10, unique=True)
    client_name = models.CharField(max_length=255)
    fotoage_link = models.URLField()
    notes = models.TextField()
    quantity = models.PositiveIntegerField()
    start_date = models.DateField()
    due_date = models.DateField()

    approval_status = models.CharField(
        max_length=10, choices=[
            ('Approved', 'Approved'),
            ('Pending', 'Pending'),
            ('Rejected', 'Rejected'),
        ],
        default='Pending'
    )

    def __str__(self):
        return f"{self.task_number} {self.client_name}"


class ToDoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description[:20]
