from django.db import models

# Create your models here.
class StudentDetail(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.roll_number})"
