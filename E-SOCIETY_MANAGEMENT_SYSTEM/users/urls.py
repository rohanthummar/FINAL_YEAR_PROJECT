from django.urls import path
from . import views

urlpatterns = [

    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("resident-dashboard/", views.resident_dashboard, name="resident_dashboard"),
    path("security-dashboard/", views.security_dashboard, name="security_dashboard"),
]