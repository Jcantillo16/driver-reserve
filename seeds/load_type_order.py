import sys, os, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.orders.models import Type_Order


def load_type_order():
    type_orders = [
        {'name': 'Package'},
        {'name': 'Document'},
        {'name': 'Food'},
        {'name': 'Medicine'},
        {'name': 'Other'},
    ]

    for type_order in type_orders:
        if not Type_Order.objects.filter(name=type_order['name']).exists():
            Type_Order.objects.create(**type_order)

    print('Type orders loaded')


load_type_order()
