from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
import json
from visitors.models import Visitor
from complaints.models import Complaint
from facilities.models import Booking
from finance.models import MaintenanceBill
from users.models import User
from django.db.models import Sum,Count
from django.db.models.functions import TruncDate



def login_view(request):

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                if user.role == "admin":
                    return redirect("admin_dashboard")

                elif user.role == "resident":
                    return redirect("resident_dashboard")

                elif user.role == "security":
                    return redirect("security_dashboard")

    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")



@login_required
def resident_dashboard(request):
    return render(request, "resident_dashboard.html")


@login_required
def security_dashboard(request):
    return render(request, "security_dashboard.html")


def admin_dashboard(request):

    total_residents = User.objects.filter(role="resident").count()
    total_visitors = Visitor.objects.count()
    total_complaints = Complaint.objects.count()

    total_revenue = MaintenanceBill.objects.filter(status="paid").aggregate(
        total=Sum('amount')
    )['total'] or 0

    # 📈 Visitors per day
    visitor_data = (
        Visitor.objects
        .annotate(date=TruncDate('visit_date'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )

    visitor_labels = [str(v['date']) for v in visitor_data]
    visitor_counts = [v['count'] for v in visitor_data]

    # 🥧 Complaint status
    complaint_data = Complaint.objects.values('status').annotate(count=Count('id'))

    complaint_labels = [c['status'] for c in complaint_data]
    complaint_counts = [c['count'] for c in complaint_data]

    context = {
    "total_residents": total_residents,
    "total_visitors": total_visitors,
    "total_complaints": total_complaints,
    "total_revenue": total_revenue,

    "visitor_labels": json.dumps(visitor_labels),
    "visitor_counts": json.dumps(visitor_counts),

    "complaint_labels": json.dumps(complaint_labels),
    "complaint_counts": json.dumps(complaint_counts),
}

    return render(request, "admin_dashboard.html", context)

@login_required
def admin_complaints(request):
    complaints = Complaint.objects.all()
    return render(request, "admin_complaints.html", {"complaints": complaints})