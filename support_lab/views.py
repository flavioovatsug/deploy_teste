from rest_framework import generics
from rest_framework import permissions
from support_lab.models import SupportTest, SupportLab
from support_lab.serializers import SupportTestSerializer, SupportLabSerializer
from users.permissions import IsOwnerOrReadOnly

class SupportLabList(generics.ListCreateAPIView):
  queryset = SupportLab.objects.all()
  serializer_class = SupportLabSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class SupportLabDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = SupportLab.objects.all()
  serializer_class = SupportLabSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class SupportTestList(generics.ListCreateAPIView):
  queryset = SupportTest.objects.all()
  serializer_class = SupportTestSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class SupportTestDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = SupportTest.objects.all()
  serializer_class = SupportTestSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]