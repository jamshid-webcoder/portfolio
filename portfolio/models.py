from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.TextField(max_length=32,)
    email = models.EmailField(verbose_name='Email address', max_length=255, unique=True)
    title = models.CharField(max_length=225)
    message = models.TextField()

    def __str__(self):
        return self.name