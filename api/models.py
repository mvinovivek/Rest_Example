from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    owner=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=50)
    note=models.CharField(max_length=1000)
    date_created=models.DateField(auto_now_add=True)  
    date_edited=models.DateField(auto_now=True)  


    def __str__(self) -> str:
        return self.title
