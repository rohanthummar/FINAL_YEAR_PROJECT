from django.urls import path
from . import views

urlpatterns = [

    path('announcements/', views.announcement_list, name='announcement_list'),

    path('create-announcement/', views.create_announcement, name='create_announcement'),

]