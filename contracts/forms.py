from django import forms
from .models import Contract

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf, .docx',
                }),
        }
        labels = {
            'file': 'Seleccione un archivo PDF o docx'
            }
        help_texts = {
            'file': 'Solo archivos PDF. tamano maximo 10MB'
            }


    def clean_file(self):
        file = self.cleaned_data.get('file')

        if file.size > 10 * 1024 * 1024:
            raise forms.ValidationError("El archivo es demasiado grande. Maximo 10MB")
        if not file.name.lower().endswith('.pdf'):
            raise forms.ValidationError("El archivo debe ser un archivo PDF")
        return file


