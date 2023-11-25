from rest_framework import serializers
from django.contrib.auth.models import User
from core.views import Patient

class UserSerializer(serializers.ModelSerializer):
   patient = serializers.PrimaryKeyRelatedField(many=True, queryset=Patient.objects.all())

   class Meta():
      model = User
      fields = ['id', 'username', 'patient']