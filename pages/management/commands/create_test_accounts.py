from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from pages.models import Client, Service
import random
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Create test accounts for the application'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=5,
            help='Number of test accounts to create (default: 5)'
        )
        parser.add_argument(
            '--admin',
            action='store_true',
            help='Create admin superuser account'
        )

    def handle(self, *args, **options):
        count = options['count']
        
        if options['admin']:
            self.create_admin_account()
        
        self.create_test_clients(count)
        self.create_test_services()
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {count} test accounts!')
        )

    def create_admin_account(self):
        """Create Django admin superuser"""
        admin_username = 'admin'
        admin_email = 'admin@wathaiqplus.com'
        admin_password = 'admin123'
        
        if not User.objects.filter(username=admin_username).exists():
            User.objects.create_superuser(
                username=admin_username,
                email=admin_email,
                password=admin_password
            )
            self.stdout.write(
                self.style.SUCCESS(f'Admin account created: {admin_username} / {admin_password}')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Admin account already exists')
            )

    def create_test_clients(self, count):
        """Create test client accounts"""
        states = [
            'الجزائر', 'وهران', 'قسنطينة', 'سطيف', 'البليدة',
            'تيزي وزو', 'باتنة', 'بجاية', 'سكيكدة', 'عنابة'
        ]
        
        genders = ['ذكر', 'أنثى']
        
        first_names = [
            'أحمد', 'محمد', 'علي', 'يوسف', 'عمر', 'خالد', 'سعد', 'طارق',
            'فاطمة', 'عائشة', 'خديجة', 'مريم', 'زينب', 'نور', 'سارة', 'ريم'
        ]
        
        last_names = [
            'بن علي', 'بن محمد', 'بن أحمد', 'بن عمر', 'بن خالد',
            'بنت علي', 'بنت محمد', 'بنت أحمد', 'بنت عمر', 'بنت خالد'
        ]

        for i in range(count):
            # Generate random data
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            full_name = f"{first_name} {last_name}"
            family_name = last_name
            
            email = f"test{i+1}@wathaiqplus.com"
            nin_number = ''.join([str(random.randint(0, 9)) for _ in range(18)])
            phone_number = f"0{random.choice([5, 6, 7])}{''.join([str(random.randint(0, 9)) for _ in range(8)])}"
            
            # Random birthday between 18-65 years ago
            start_date = date.today() - timedelta(days=65*365)
            end_date = date.today() - timedelta(days=18*365)
            random_days = random.randint(0, (end_date - start_date).days)
            birthday = start_date + timedelta(days=random_days)
            
            state = random.choice(states)
            gender = random.choice(genders)
            password = 'test123456'  # Simple password for testing
            
            # Create client if doesn't exist
            if not Client.objects.filter(email=email).exists():
                Client.objects.create(
                    nin_number=nin_number,
                    phone_number=phone_number,
                    birthday=birthday,
                    state=state,
                    family_name=family_name,
                    full_name=full_name,
                    email=email,
                    gender=gender,
                    password=make_password(password)
                )
                self.stdout.write(f'Created test client: {full_name} ({email}) - Password: {password}')

    def create_test_services(self):
        """Create sample service requests for test clients"""
        clients = Client.objects.all()
        service_types = [
            'passport', 'id_card', 'nationality', 'bills', 'visas',
            'consulting', 'notary_lawyer', 'insurance', 'business_license', 'other'
        ]
        
        for client in clients[:3]:  # Create services for first 3 clients
            # Create 1-3 services per client
            num_services = random.randint(1, 3)
            for _ in range(num_services):
                service_type = random.choice(service_types)
                status = random.choice(['En attente', 'Approuvé', 'Rejeté'])
                
                Service.objects.create(
                    user=client,
                    service_type=service_type,
                    additional_text=f"طلب تجريبي للخدمة: {service_type}",
                    status=status
                )
        
        self.stdout.write('Created sample service requests for test clients')
