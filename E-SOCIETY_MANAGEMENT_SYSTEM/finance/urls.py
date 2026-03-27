from django.urls import path
from . import views

urlpatterns = [

    path('my-bills/', views.resident_bills, name='resident_bills'),

    path('pay-bill/<int:bill_id>/', views.pay_bill, name='pay_bill'),

    path('admin-bills/', views.admin_bills, name='admin_bills'),

    path('create-bill/', views.create_bill, name='create_bill'),

]