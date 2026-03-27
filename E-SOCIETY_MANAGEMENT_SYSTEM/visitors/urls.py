from django.urls import path
from . import views

urlpatterns = [

    path('create-visitor/', views.create_visitor, name='create_visitor'),

    path('visitor-list/', views.visitor_list, name='visitor_list'),

     path('security-visitors/', views.security_visitors, name='security_visitors'),

    path('approve-visitor/<int:visitor_id>/', views.approve_visitor, name='approve_visitor'),

    path('reject-visitor/<int:visitor_id>/', views.reject_visitor, name='reject_visitor'),

]
