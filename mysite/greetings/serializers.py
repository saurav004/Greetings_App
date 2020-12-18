from rest_framework import serializers
from .models import GreetingClass


class GreetingClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreetingClass
        fields = '__all__'
