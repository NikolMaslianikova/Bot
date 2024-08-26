from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medicine/', include('Medicine.urls')),
]
urlpatterns += url

