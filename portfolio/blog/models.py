from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

class Blogpost(models.Model):
    content = RichTextField()