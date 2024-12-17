from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_sistema.urls'))
]

#REST FRAMEWORK URL
# path('api/', include('app_sistema.api.urls', 'app_sistema_api'))
