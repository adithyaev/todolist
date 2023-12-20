from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    completed_date = models.CharField(max_length = 20,default = 'incomplete')
    status = models.CharField(max_length = 10,default = 'pending')
    date = models.CharField(max_length = 20,default = '')
    
    class Meta:
        db_table = 'task_tb'
    
    
