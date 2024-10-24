from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

TASK_PRIORITIES = [
    ("bl", "🔴 Blocker"),
    ("cr", "🟠 Critical"),
    ("mj", "🟡 Major"),
    ("mn", "🟢 Minor"),
    ("tr", "🔵 Trivial")
]


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, )

    def get_absolute_url(self):
        return reverse("task_manager:worker-detail", kwargs={"pk": self.pk})


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    deadline = models.DateField(null=True)
    is_completed = models.BooleanField()
    priority = models.CharField(max_length=2, choices=TASK_PRIORITIES)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="tasks")

    def __str__(self):
        return self.name
