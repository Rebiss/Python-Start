from django.db import models

class Task(models.Model):
    title = models.CharField('name', max_length=55)
    task = models.TextField('description')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'