from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    status = ForeignKey('task_status', default=None, null=True, on_delete=models.CASCADE)
    user = ForeignKey('auth.user', default=None, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class task_status(models.Model):
    status_name = CharField(max_length=50)

    def __str__(self):
        return self.status_name