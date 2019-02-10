from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('food/<int:pk>/', views.food_edit, name='food_edit'),
    path('cashier_list/1/', views.cashier1, name='cashier'),
]
