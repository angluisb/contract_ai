from django.core.validators import FileExtensionValidator
from django.db import models
from users.models import User
# Create your models here.

def contract_upload_path(instance, filename):
    """Función para definir la ruta de subida de contratos"""
    return f"contracts/{instance.user.username}/{filename}"

class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_filename = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to= contract_upload_path, validators=[FileExtensionValidator(allowed_extensions=['pdf','docx'])])
    upload_at = models.DateTimeField(auto_now_add=True)
    extracted_text = models.TextField(blank=True)
    analysis_result = models.TextField(blank=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-upload_at']

    def save(self, *args, **kwargs):
        if self.file:  # Si hay un archivo
            self.original_filename = self.file.name  # Guardar nombre original
        super().save(*args, **kwargs)  # Guardar normalmente

    def __str__(self):
        return f"Contrato de {self.user.username} - {self.original_filename}"

class ContractQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='qas')
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'contract','created_at']),
        ]

    def __str__(self):
        return f"Q&A de {self.user.username} para el contrato {self.contract.original_filename}"
