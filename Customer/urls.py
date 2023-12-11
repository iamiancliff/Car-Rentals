from django.urls import path
from Customer.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('auth/', auth_view, name='auth_view'),
    path('logout/', logout_view, name='logout_view'),
    path('register/', register, name='register'),
    path('registration/', registration, name='registration'),
    path('search/', search, name='search'),
    path('search_results/', search_results, name='search_results'),
    path('rent/', rent_vehicle, name='rent_vehicle'),
    path('confirmed/', confirm, name='confirm'),
    path('manage/', manage, name='manage'),
    path('update/', update_order, name='update_order'),
    path('delete/', delete_order, name='delete_order'),
]
