# forms.py
from django import forms
from .models import Client
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Client
        fields = ['nin_number', 'phone_number', 'birthday', 'state', 'family_name', 'full_name', 'email', 'gender', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")


# forms.py
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_type', 'uploaded_file', 'additional_text']
        labels = {
            'service_type': 'نوع الخدمة',
            'uploaded_file': 'الملف المرفوع',
            'additional_text': 'نص إضافي',
        }