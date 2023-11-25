from django.db import models
from cpf_field.models import CPFField
from django.contrib.postgres.fields import ArrayField


class Patient(models.Model):
 
  GENDER_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino')
  )

  created = models.DateTimeField(auto_now_add=True)
  code = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
  birth_date = models.DateField()
  personal_id_number = CPFField('cpf', unique=True)
  phone_number = models.CharField(max_length=20)
  owner = models.ForeignKey('auth.User', related_name='patient', on_delete=models.CASCADE)

  class Meta:
    ordering = ['created']

class InternalTest(models.Model):
  id = models.AutoField(primary_key=True)
  created = models.DateTimeField(auto_now_add=True)
  code = models.CharField(max_length=20)
  name = models.CharField(max_length=150)
  alias = ArrayField(models.CharField(max_length=200), blank=True, default=list)
  description = models.TextField(max_length=500)
  deadline_in_hours = models.DurationField()
  sales_price = models.DecimalField(max_digits=10, decimal_places=2)
  on_sale = models.BooleanField(default=False)
  owner = models.ForeignKey('auth.User', related_name='internal_lab_tests', on_delete=models.CASCADE)

  class Meta:
    ordering = ['created']