from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view
from django.urls import re_path
from django.urls import re_path
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views


urlpatterns = [
   path('patient/', views.PatientList.as_view()),
   path('patient/<int:pk>/', views.PatientDetail.as_view()),
   path('internaltest/', views.InternalTestList.as_view()),
   path('internaltest/<int:pk>/', views.InternalTestDetail.as_view()),

]

schema_view = get_swagger_view(title='User API')
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns += [
   re_path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = format_suffix_patterns(urlpatterns)