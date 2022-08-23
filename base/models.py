from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    major = models.CharField(max_length=500)

    def __str__(self):
        return self.name
        