from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    facultyName = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created']