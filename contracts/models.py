from django.core.validators import FileExtensionValidator
from django.db import models
from users.models import User
# Create your models here.

class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_filename = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='contracts/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
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


