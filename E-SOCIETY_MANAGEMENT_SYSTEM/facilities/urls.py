from django.urls import path
from . import views

urlpatterns = [

    path('create-booking/', views.create_booking, name='create_booking'),

    path('booking-list/', views.booking_list, name='booking_list'),

    path('approve-booking/<int:booking_id>/', views.approve_booking, name='approve_booking'),

    path('reject-booking/<int:booking_id>/', views.reject_booking, name='reject_booking'),
    

]