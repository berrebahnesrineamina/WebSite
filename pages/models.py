from django.db import models
from django.contrib.auth.models import User  # si tu en as besoin ailleurs
from django.utils import timezone


class Client(models.Model):
    nin_number = models.CharField(max_length=18, unique=True)
    phone_number = models.CharField(max_length=15)
    birthday = models.DateField()
    state = models.CharField(max_length=30)
    family_name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=56)
    password = models.CharField(max_length=128) 

    def __str__(self):
        return f"{self.full_name} ({self.email})"

# ...

class PendingClient(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6)
    full_name = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    nin_number = models.CharField(max_length=18)
    phone_number = models.CharField(max_length=15)
    birthday = models.DateField()
    state = models.CharField(max_length=30)
    family_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=56)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.email} - Code: {self.code}"

class Service(models.Model):
    SERVICE_TYPES = [
        ('passport', 'إستخراج وثائق رسمية - جواز السفر'),
        ('id_card', 'إستخراج وثائق رسمية - بطاقة الهوية الوطنية البيومترية'),
        ('nationality', 'إستخراج وثائق رسمية - الجنسية'),
        ('bills', 'دفع الفواتير و المستحقات الرسمية'),
        ('visas', 'تجهيز طلبات و ملفات مختلفة - تأشيرات'),
        ('consulting', 'الإستشارات الإدارية'),
        ('notary_lawyer', 'مكاتب التوثيق و المحاماة'),
        ('insurance', 'خدمات التأمين الصحي و تأمين السيارات'),
        ('business_license', 'إصدار رخص تجارية و توفير وكيل خدمات المواطن'),
        ('construction_license', 'إصدار رخصة البناء'),
        ('other', 'طلبات أخرى'),
    ]
    
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='services')
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    uploaded_file = models.FileField(upload_to='service_files/')
    additional_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
    ('En attente', 'En attente'),
    ('Approuvé', 'Approuvé'),
    ('Rejeté', 'Rejeté'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='En attente')

    def __str__(self):
        return f"{self.service_type} - {self.user.full_name}"
