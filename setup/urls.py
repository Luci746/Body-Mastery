from django.contrib import admin
from django.urls import path, include
import usuarios.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(usuarios.urls)),

]
