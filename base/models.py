from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=300)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)


def __word__(self):
    return self.title

class Meta:
    ordering=['complete']
