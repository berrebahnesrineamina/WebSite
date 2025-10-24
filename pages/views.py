# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Client, PendingClient, Service
from .forms import ServiceForm
import random
from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from .models import Service, Client
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


def home(request):
    return render(request, 'pages/home.html')

def signup(request):
    storage = messages.get_messages(request)
    for _ in storage:
        pass  # juste pour vider
    if request.method == 'POST':
        print("POST reçu avec données :", request.POST)
        nin = request.POST.get('nin_number')
        phone = request.POST.get('phone_number')
        birthday = request.POST.get('birthday')
        state = request.POST.get('state')
        family_name = request.POST.get('family_name')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        print("Données reçues :", nin, phone, birthday, state, family_name, full_name, email, gender)
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if Client.objects.filter(email=email).exists() or PendingClient.objects.filter(email=email).exists():
            messages.error(request, "Email already used.")
            return redirect('signup')

        code = str(random.randint(100000, 999999))

        pending = PendingClient.objects.create(
            email=email,
            full_name=full_name,
            password=make_password(password),
            nin_number=nin,
            phone_number=phone,
            birthday=birthday,
            state=state,
            family_name=family_name,
            gender=gender,
            code=code
        )

        send_mail(
            subject='Confirmation Code - وثائق+',
            message=f'Your confirmation code is: {code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        request.session['pending_email'] = email
        # messages.success(request, "Confirmation code sent to your email.")
        messages.success(request, "Confirmation code sent to your email.", extra_tags='registration')
        return redirect('confirm_email')  # Une autre vue à créer
    return render(request, 'pages/registration.html')

def confirm_email(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        email = request.session.get('pending_email')

        try:
            pending = PendingClient.objects.get(email=email, code=code)
        except PendingClient.DoesNotExist:
            messages.error(request, "Invalid code.")
            return redirect('confirm_email')

        # Créer le client confirmé
        Client.objects.create(
            email=pending.email,
            full_name=pending.full_name,
            password=pending.password,
            nin_number=pending.nin_number,
            phone_number=pending.phone_number,
            birthday=pending.birthday,
            state=pending.state,
            family_name=pending.family_name,
            gender=pending.gender
        )

        pending.delete()
        messages.success(request, "Email verified and account created.")
        return redirect('login')

    return render(request, 'pages/confirm_email.html')


def reset_password1(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(f"Demande de reset pour email: {email}")

        try:
            client = Client.objects.get(email=email)
            code = str(random.randint(100000, 999999))
            print(f"Code généré: {code} pour {email}")

            request.session['reset_email'] = email
            request.session['reset_code'] = code

            send_mail(
                subject='Password Reset Code - وثائق+',
                message=f'Your password reset code is: {code}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )

            messages.success(request, 'Reset code sent to your email.')
            return redirect('reset_password2')

        except Client.DoesNotExist:
            messages.error(request, 'No account found with this email.')
            return redirect('reset_password1')

    return render(request, 'pages/1_reset_password_form.html')
def reset_password2(request):
    if request.method == 'POST':
        # Récupérer les 6 chiffres entrés individuellement
        digit1 = request.POST.get('digit1')
        digit2 = request.POST.get('digit2')
        digit3 = request.POST.get('digit3')
        digit4 = request.POST.get('digit4')
        digit5 = request.POST.get('digit5')
        digit6 = request.POST.get('digit6')

        # Construire le code complet
        entered_code = ''.join([digit1, digit2, digit3, digit4, digit5, digit6])
        saved_code = request.session.get('reset_code')

        print(f"Code entré: {entered_code}, code attendu: {saved_code}")

        # Comparer avec le code stocké
        if entered_code == saved_code:
            messages.success(request, 'Code correct. You can now reset your password.')
            return redirect('reset_password3')
        else:
            messages.error(request, 'Invalid code.')
            return redirect('reset_password2')

    return render(request, 'pages/2_reset_password_check_email.html')
def reset_password3(request):
    if request.method == "POST":
        new_password = request.POST.get("new_password")
        user_email = request.session.get("reset_email")

        if not user_email:
            return redirect('reset_password1')

        try:
            client = Client.objects.get(email=user_email)  # ⚠️ tu utilises Client et pas User
            client.password = make_password(new_password)
            client.save()

            # Nettoyage session
            request.session.pop("reset_email", None)
            request.session.pop("reset_code", None)

            return redirect('reset_password4')  # Vers la page de confirmation

        except Client.DoesNotExist:
            return redirect('reset_password1')

    return render(request, 'pages/3_reset_password_reset_password.html')
def reset_password4(request):
    # Plus de vérification ni redirection — simplement afficher le template
    return render(request, 'pages/4_reset_password_confirmation.html')


def login_client(request):
    if request.method == 'POST':
        print("🔐 Requête POST reçue pour login")
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"📥 Données reçues : email={email}, password={password}")

        try:
            client = Client.objects.get(email=email)
            print(f"✅ Utilisateur trouvé : {client.full_name} (ID: {client.id})")
        except Client.DoesNotExist:
            print("❌ Aucun utilisateur trouvé avec cet email.")
            messages.error(request, "Email not found.")
            return redirect('login')

        if check_password(password, client.password):
            print("🔑 Mot de passe correct. Connexion réussie.")
            request.session['client_id'] = client.id
            messages.success(request, f"Welcome {client.full_name}!")
            return redirect('home_user') 
        else:
            print("🚫 Mot de passe incorrect.")
            messages.error(request, "Incorrect password.")
            return redirect('login')

    print("📄 Requête GET reçue pour la page de login")
    return render(request, 'pages/login.html')

def logout_view(request):
    # Supprimer la session ou utiliser logout() de django.contrib.auth
    request.session.flush()
    return redirect('login')
def logout_admin(request):
    # Supprimer la session ou utiliser logout() de django.contrib.auth
    request.session.flush()
    return redirect('admin_login')

def add_service(request):
    client_id = request.session.get('client_id')
    if not client_id:
        print("⛔ Utilisateur non connecté.")
        return redirect('login')

    try:
        client = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        print("❌ Client ID invalide.")
        return redirect('login')

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = client  # ✅ ici on utilise le client de la session, pas request.user
            service.save()
            return redirect('home_user')
        else:
            print("⚠️ Formulaire invalide :", form.errors)
    else:
        form = ServiceForm()

    return render(request, 'pages/add_service.html', {'form': form})

def delete_service(request, service_id):
    client_id = request.session.get('client_id')
    if not client_id:
        return redirect('login')

    service = get_object_or_404(Service, id=service_id, user_id=client_id)

    if request.method == 'POST':
        service.delete()
        messages.success(request, "Service deleted successfully.")
    
    return redirect('home_user')


def home_user(request):
    client_id = request.session.get('client_id')
    if not client_id:
        return redirect('login')

    try:
        client = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return redirect('login')

    services = Service.objects.filter(user=client)  # ✅ tous les services de ce client

    return render(request, 'pages/home_user.html', {'services': services, 'client': client})


def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user = authenticate(username=user.username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('home_admin')
            else:
                return render(request, 'pages/login_admin.html', {'error': 'Invalid credentials or not admin'})
        except User.DoesNotExist:
            return render(request, 'pages/login_admin.html', {'error': 'Email not found'})
    return render(request, 'pages/login_admin.html')

def home_admin(request):
    services = Service.objects.select_related('user').all()
    return render(request, 'pages/home_admin.html', {'services': services})



def check_request(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    client = service.user  # le client lié à ce service

    if request.method == 'POST':
        if 'accept' in request.POST:
            service.status = 'Approuvé'
            service.save()
            messages.success(request, "La demande a été approuvée.")
            return redirect('home_admin')

        elif 'reject' in request.POST:
            reason = request.POST.get('reason', '').strip()
            if not reason:
                messages.error(request, "Veuillez saisir la cause du refus avant de confirmer.")
                return render(request, 'pages/check_request.html', {
                    'client': client,
                    'service': service,
                })
            # Stocker la raison dans la session et rediriger vers reject_request
            request.session['rejection_reason'] = reason
            return redirect('reject_request', service_id=service.id)

    return render(request, 'pages/check_request.html', {
        'client': client,
        'service': service,
    })


def reject_request(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    reason = request.session.pop('rejection_reason', 'Non spécifiée')

    service.status = 'Rejeté'
    service.save()

    subject = 'Votre demande a été rejetée'
    message = f"""
مرحبًا {service.user.full_name}،

لقد تم رفض طلبك للخدمة "{service.get_service_type_display()}".

سبب الرفض:
{reason}

إذا كانت لديك أي استفسارات، فلا تتردد في التواصل معنا.

مع أطيب التحيات،
الفريق الإداري
"""
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [service.user.email]

    send_mail(subject, message, from_email, recipient_list)

    messages.warning(request, "La demande a été rejetée et un email a été envoyé à l'utilisateur.")
    return redirect('home_admin')
