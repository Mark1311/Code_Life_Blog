from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CodeLife(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_to = models.DateTimeField(auto_created=True)
    updated_to = models.DateTimeField(auto_created=True)



    def __str__(self):
        return f'{self.user.username} - {self.test[:10]}'
    
    