from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('allauth.urls')),
    path('suptests/', include('support_lab.urls')),
    path('Users/', include('users.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
