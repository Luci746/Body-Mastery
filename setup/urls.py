from django.contrib import admin
from django.urls import path, include
import usuarios.urls, suporte.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include(usuarios.urls)),
    path('suporte/', include(suporte.urls))

]
