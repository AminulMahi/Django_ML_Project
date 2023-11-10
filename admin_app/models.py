from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class blog(models.Model):  # class and function name cannot be same
    image = models.ImageField(upload_to='images/')
    date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    description = RichTextField()
    