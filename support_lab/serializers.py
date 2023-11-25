from rest_framework import serializers
from support_lab.models import SupportTest, SupportLab

class SupportLabSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source ='owner.username')

  class Meta():
    model = SupportLab
    fields = ['created', 'id', 'name', 'integration_code', 'integration_system_version', 'owner']

class SupportTestSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source ='owner.username')

  class Meta():
    model = SupportTest
    fields = '__all__'
    #fields = ['created', 'id', 'code', 'name', 'deadline_in_hours', 'sales_price', 'on_sale']