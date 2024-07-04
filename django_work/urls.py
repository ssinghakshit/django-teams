from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),  # Projects app URL
    path('users/', include('users.urls')),        # Users app URL
]
