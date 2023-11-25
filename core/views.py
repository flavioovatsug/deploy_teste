from core.models import Patient, InternalTest
from core.serializers import PatientSerializer, InternalTestSerializer
from rest_framework import generics
from rest_framework import permissions
from users.permissions import IsOwnerOrReadOnly
from datetime import date
from rest_framework.response import Response
from rest_framework import status


#Cria a instancia e lista todas
class PatientList(generics.ListCreateAPIView):
  queryset = Patient.objects.all()
  serializer_class = PatientSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def create(self, request, *args, **kwargs):
    birth_date = request.data.get('birth_date')
    if birth_date:
      today = date.today()
      birth_date = date.fromisoformat(birth_date)
      age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
      if age < 18:
        return Response({'detail': 'Como o paciente não tem mais de 18 anos, coloce o cpf do responsável.'}, status=status.HTTP_400_BAD_REQUEST)
    return super().create(request, *args, **kwargs)
  
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


#Edita e exclui a instancia
class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Patient.objects.all()
  serializer_class = PatientSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class InternalTestList(generics.ListCreateAPIView):
  queryset = InternalTest.objects.all()
  serializer_class = InternalTestSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class InternalTestDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = InternalTest.objects.all()
  serializer_class = InternalTestSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
