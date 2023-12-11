from django.urls import path, include
from Car_dealer.views import *
from django.urls import path

urlpatterns = [
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('auth/', auth_view, name='auth_view'),
    path('logout/', logout_view, name='logout_view'),
    path('register/', register, name='register'),
    path('registration/', registration, name='registration'),
    path('add_vehicle/', add_vehicle, name='add_vehicle'),
    path('manage_vehicles/', manage_vehicles, name='manage_vehicles'),
    path('order_list/', order_list, name='order_list'),
    path('complete/', complete, name='complete'),
    path('history/', history, name='history'),
    path('delete/', delete, name='delete'),
]
