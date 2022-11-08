import sys, os, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.payment.models import PaymentMethod


def load_payment_methods():
    payment_methods = [
        {'name': 'Cash'},
        {'name': 'Credit card'},
        {'name': 'Debit card'},
        {'name': 'Wire Transfer'},
        {'name': 'Check'},
    ]

    for payment_method in payment_methods:
        if not PaymentMethod.objects.filter(name=payment_method['name']).exists():
            PaymentMethod.objects.create(**payment_method)

    print('Payment methods loaded')


load_payment_methods()
