from django.urls import path
from suporte import views

urlpatterns = [
    path('contato/', views.contato, name='contato'),

]
