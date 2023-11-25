from core.models import Patient, InternalTest
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
   owner = serializers.ReadOnlyField(source='owner.username')

   class Meta():
      model = Patient
      fields = ['created', 'code', 'name', 'birth_date', 'sex', 'personal_id_number', 'phone_number', 'owner']

class InternalTestSerializer(serializers.ModelSerializer):
   owner = serializers.ReadOnlyField(source ='owner.username')

   class Meta():
      model = InternalTest
      fields = ['created', 'id', 'code', 'name', 'description', 'deadline_in_hours', 'sales_price', 'on_sale']