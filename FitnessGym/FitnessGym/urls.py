from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/',
        include([
            path('admin/', admin.site.urls),
            path('', include('api.urls')),
        ])
    ),
]
