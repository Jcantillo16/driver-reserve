from rest_framework import serializers
from apps.customers.models import Customer
from cryptography.fernet import Fernet
from io import BytesIO


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def generate_and_save_key(self, validated_data):
        key = Fernet.generate_key()
        validated_data['key'] = key
        return validated_data

    def encrypt_password(self, validated_data):
        password = validated_data['password']
        key = validated_data['key']
        f = Fernet(key)
        encrypted_password = f.encrypt(password.encode())
        validated_data['password'] = encrypted_password
        return validated_data

    def create(self, validated_data):
        validated_data = self.generate_and_save_key(validated_data)
        validated_data = self.encrypt_password(validated_data)
        return super().create(validated_data)

    # login
    def decrypt_password(self, key, encrypted_password):
        key = key.split("'")[1].encode()
        encrypted_password = encrypted_password.split("'")[1].encode()
        f = Fernet(key)
        decrypted_password = f.decrypt(encrypted_password).decode()
        return decrypted_password


    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data = self.encrypt_password(validated_data)
            return super().update(instance, validated_data)

        elif 'name' in validated_data:
            instance.name = validated_data['name']
            instance.save()
            return instance

        elif 'email' in validated_data:
            instance.email = validated_data['email']
            instance.save()
            return instance

        elif 'phone' in validated_data:
            instance.phone = validated_data['phone']
            instance.save()
            return instance
