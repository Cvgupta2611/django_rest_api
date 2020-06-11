from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=60)
    roll_no = models.CharField(max_length=60,unique=True)
    collage = models.CharField(max_length=60)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE,null=True)
    # highlighted = models.TextField(unique=False,null=True)

    def __str__(self):
        return self.name


