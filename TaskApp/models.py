from asyncio import Task
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TasksTable(models.Model):
    TaskID = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.TaskID}"

class TaskStatusTable(models.Model):
    TaskID = models.ForeignKey(TasksTable, on_delete=models.CASCADE) #TasksTable id as foreignkey
    UserID = models.ForeignKey(User, on_delete=models.CASCADE) # User table id as foreignkey
    TStatus = models.CharField(max_length=255, choices=(('NotStarted', 'NotStarted'),('InProgress', 'InProgress'),('Completed','Completed')))

    