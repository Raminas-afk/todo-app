from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    importance = models.IntegerField(default=3, validators=[MaxValueValidator(10), MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

        