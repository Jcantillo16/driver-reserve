from django.test import TestCase
from .models import Customer


class CustomerTestCase(TestCase):
    def setUp(self):
        customer = Customer.objects.create(
            name='juan',
            phone='123456789',
            email='juancantillo1317@gmail.com',
            password='123456789'
        )
        customer.save()

    def test_customer(self):
        customer = Customer.objects.get(name='juan')
        self.assertEqual(customer.name, 'juan')
        self.assertEqual(customer.phone, '123456789')
        self.assertEqual(customer.email, 'juancantillo1317@gmail.com')
        self.assertEqual(customer.password, '123456789')

    def test_customer_update(self):
        customer = Customer.objects.get(name='juan')
        customer.name = 'juan2'
        customer.save()
        self.assertEqual(customer.name, 'juan2')

    def test_customer_delete(self):
        customer = Customer.objects.get(name='juan')
        customer.delete()
        self.assertEqual(Customer.objects.count(), 0)

    def test_customer_list(self):
        customer = Customer.objects.all()
        self.assertEqual(customer.count(), 1)

    def test_customer_detail(self):
        customer = Customer.objects.get(name='juan')
        self.assertEqual(customer.name, 'juan')
        self.assertEqual(customer.phone, '123456789')
        self.assertEqual(customer.email, 'juancantillo1317@gmail.com')
        self.assertEqual(customer.password, '123456789')

    def test_customer_login(self):
        customer = Customer.objects.get(name='juan')
        customer.is_logged = True
        customer.save()
        self.assertEqual(customer.is_logged, True)

    def test_customer_logout(self):
        customer = Customer.objects.get(name='juan')
        customer.is_logged = False
        customer.save()
        self.assertEqual(customer.is_logged, False)

    def test_customer_key(self):
        customer = Customer.objects.get(name='juan')
        customer.key = '123456789'
        customer.save()
        self.assertEqual(customer.key, '123456789')

    def test_customer_password(self):
        customer = Customer.objects.get(name='juan')
        customer.password = '123456789'
        customer.save()
        self.assertEqual(customer.password, '123456789')

    def test_customer_email(self):
        customer = Customer.objects.get(name='juan')
        customer.email = 'juancantillo1317@gmail.com'
        customer.save()
        self.assertEqual(customer.email, 'juancantillo1317@gmail.com')

    def test_customer_phone(self):
        customer = Customer.objects.get(name='juan')
        customer.phone = '123456789'
        customer.save()
        self.assertEqual(customer.phone, '123456789')

    def test_customer_name(self):
        customer = Customer.objects.get(name='juan')
        customer.name = 'juan'
        customer.save()
        self.assertEqual(customer.name, 'juan')

    def test_customer_id(self):
        customer = Customer.objects.get(name='juan')
        self.assertEqual(customer.id, 1)

    def test_customer_str(self):
        customer = Customer.objects.get(name='juan')
        self.assertEqual(customer.__str__(), 'juan')
