from django.urls import path
from . import views

urlpatterns = [

    path('create-complaint/', views.create_complaint, name='create_complaint'),

    path('complaint-list/', views.complaint_list, name='complaint_list'),

     path('admin-complaints/', views.admin_complaints, name='admin_complaints'),

    path(
        'update-complaint/<int:complaint_id>/<str:status>/',
        views.update_complaint_status,
        name='update_complaint_status'
    ),
]