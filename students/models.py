from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return self.name