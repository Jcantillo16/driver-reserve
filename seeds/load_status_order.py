import sys, os, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.orders.models import Status_Order


def load_status_order():
    status_orders = [
        {'name': 'Pending'},
        {'name': 'In Progress'},
        {'name': 'Finished'},
        {'name': 'Canceled'},
    ]

    for status_order in status_orders:
        if not Status_Order.objects.filter(name=status_order['name']).exists():
            Status_Order.objects.create(**status_order)

    print('Status orders loaded')


load_status_order()
