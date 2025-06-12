from django.db import models
from users.models import User
# Create your models here.

class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='contracts/')
    upload_at = models.DateTimeField(auto_now_add=True)
    extracted_text = models.TextField(blank=True)
    analysis_result = models.TextField(blank=True)

    def __str__(self):
        return f"Contrato de {self.user.username}"
