from django.contrib import admin
from django.urls import path, include
from .views import home  # Make sure this import matches step 1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('', home),  # Root URL now works
]