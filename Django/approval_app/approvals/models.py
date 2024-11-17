from django.db import models
import os
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

# Create your models here.

class Process(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProcessCode(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name="codes")
    code_name = models.CharField(max_length=100)

    def __str__(self):
        return self.code_name
    
    def clean(self):
        # Check if a ProcessCode with this code_name already exists for any process
        if ProcessCode.objects.filter(code_name=self.code_name).exists():
            raise ValidationError(f"The Process Code '{self.code_name}' already exists.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class UploadedFile(models.Model):
    process_code = models.ForeignKey(ProcessCode, on_delete=models.CASCADE, related_name="uploads")
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} for {self.process_code.code_name}"
    
    def delete(self, *args, **kwargs):
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)

class Approver(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ApprovalLevel(models.Model):
    process_code = models.ForeignKey(ProcessCode, on_delete=models.CASCADE, related_name="approval_levels")
    level_number = models.IntegerField()
    approver = models.CharField(max_length=100)

    def __str__(self):
        return f"Level {self.level_number} - {self.approver} - {self.process_code} - {self.process_code.process}"
    