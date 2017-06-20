from __future__ import unicode_literals

from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=140)
    description = models.CharField(max_length=10000)
    
    creation_date = models.DateTimeField('date task was created')
    deadline = models.DateTimeField("date task is scheduled to be completed")
    
    additional_notes = models.CharField(max_length=20000,blank=True,null=True)
    
    PRIORITIES=(("h","High"),('n',"Normal"),('l',"Low"))
    priority = models.CharField(max_length=6,choices=PRIORITIES,default='n')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
