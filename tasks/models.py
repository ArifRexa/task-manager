from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    # images = models.ManyToManyField('Image', related_name='associated_tasks', blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TaskImage(models.Model):
    tasks = models.ForeignKey(Task, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='task_images/')

    # def __str__(self):
    #     return self.images.name