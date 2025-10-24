"""
Email Configuration for Wathaiq Plus
Professional email settings for production
"""

# Professional email configuration
EMAIL_CONFIG = {
    'DEFAULT_FROM_EMAIL': 'noreply@wathaiqplus.com',
    'DEFAULT_FROM_NAME': 'وثائق+ (Wathaiq Plus)',
    'REPLY_TO_EMAIL': 'support@wathaiqplus.com',
}

# Email templates
EMAIL_TEMPLATES = {
    'confirmation': {
        'subject': 'رمز التأكيد - وثائق+',
        'subject_en': 'Confirmation Code - Wathaiq Plus',
    },
    'password_reset': {
        'subject': 'إعادة تعيين كلمة المرور - وثائق+',
        'subject_en': 'Password Reset - Wathaiq Plus',
    },
    'service_rejected': {
        'subject': 'تم رفض طلبك - وثائق+',
        'subject_en': 'Your Request Has Been Rejected - Wathaiq Plus',
    }
}
