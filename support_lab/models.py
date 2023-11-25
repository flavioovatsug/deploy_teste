from django.db import models
from django.contrib.postgres.fields import ArrayField

'''
import json
def default_empty_list():
  return [] #Para resolver o problema de passar uma lista vazia por padrão no field
'''

class SupportLab(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  integration_code = models.CharField(max_length=50)
  name = models.CharField(max_length=100)
  integration_system_version = models.CharField(max_length=100, blank=True)
  owner = models.ForeignKey('auth.User', related_name='SupLab', on_delete=models.CASCADE)

  class Meta:
    ordering = ['created']

  def __str__(self):
    return self.name

class SupportTest(models.Model):
  lab = models.ForeignKey(SupportLab, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  code = models.CharField(max_length=20)
  name = models.CharField(max_length=150)
  alias = ArrayField(models.CharField(max_length=200), blank=True, default=list)
  sales_price = models.DecimalField(max_digits=10, decimal_places=2)
  deadline_in_hours = models.DurationField()
  on_sale = models.BooleanField(default=False)
  owner = models.ForeignKey('auth.User', related_name='SupTest', on_delete=models.CASCADE)

  '''
  alias = models.TextField(default=default_empty_list)
  def set_my_field(self, alias):
    self.alias = json.dumps(alias)

  def get_my_field(self):
    return json.loads(self.alias)
  '''
  
  class Meta:
    ordering = ['created']