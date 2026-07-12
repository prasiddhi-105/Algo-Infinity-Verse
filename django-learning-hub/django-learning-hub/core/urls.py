from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # This adds http://127.0.0.1:8000/api/topics/
    path('', include('hub.urls')),
]