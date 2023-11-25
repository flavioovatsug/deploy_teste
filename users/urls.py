from . import views
from django.urls import path

urlpatterns = [
   path('users/', views.UserList.as_view()),
   path('users/<int:pk>/', views.UserDetail.as_view()),
]