from django.urls import path
from . import views

urlpatterns = [
  path('labs/', views.SupportLabList.as_view()),
  path('labs/<int:pk>/', views.SupportLabDetail.as_view()),  
  path('tests/', views.SupportTestList.as_view()),
  path('tests/<int:pk>/', views.SupportTestDetail.as_view()),
]