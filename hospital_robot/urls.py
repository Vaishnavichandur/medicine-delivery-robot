from django.urls import path
from delivery import views  

urlpatterns = [
    path('medicine_delivery/', views.home, name='medicine_delivery'),
    path('', views.home, name='home'),  
]
