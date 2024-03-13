from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=30)
    active=models.BooleanField(default=True)
    budget=models.IntegerField()

    def __str__(self):
        return self.name
