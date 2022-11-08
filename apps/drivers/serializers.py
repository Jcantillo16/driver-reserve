from rest_framework import serializers

from .models import Driver, LocationDriver


class LocationdriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationDriver
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    location = LocationdriversSerializer(many=True, read_only=True)

    class Meta:
        model = Driver
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'lat' in validated_data or 'lng' in validated_data:
            raise serializers.ValidationError("Unable to update latitude and longitude.d")

        elif 'is_available' in validated_data:
            raise serializers.ValidationError("Unable to update availability.")

        elif 'lastUpdate' in validated_data:
            raise serializers.ValidationError("Unable to update last update.")

        elif 'name' in validated_data:
            instance.name = validated_data['name']

        instance.save()
        return instance
