import smtplib
from email.mime.text import MIMEText

sender = "fakhreddinechaib@gmail.com"
receiver = "fakhreddinechaib@gmail.com"  # Tu testes sur toi-même
password = "cjeonrajjuitvjlf"  # mot de passe d'application Gmail

msg = MIMEText("Ceci est un test d'envoi d'email via Python.")
msg["Subject"] = "Test Email Django"
msg["From"] = sender
msg["To"] = receiver

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, [receiver], msg.as_string())
    print("✅ Email envoyé avec succès.")
except Exception as e:
    print("❌ Erreur:", e)
