from django.db import models

# Create your models here.
class Foo(models.Model):
    bar = models.CharField(max_length=120)