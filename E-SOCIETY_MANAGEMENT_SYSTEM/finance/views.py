from django.shortcuts import render, redirect, get_object_or_404
from .models import MaintenanceBill
from django.contrib.auth import get_user_model
User = get_user_model()

def resident_bills(request):

    bills = MaintenanceBill.objects.filter(resident=request.user)

    return render(request, "resident_bills.html", {"bills": bills})


def pay_bill(request, bill_id):

    bill = get_object_or_404(MaintenanceBill, id=bill_id)

    bill.status = "paid"
    bill.save()

    return redirect("resident_bills")


def admin_bills(request):

    bills = MaintenanceBill.objects.all()

    return render(request, "admin_bills.html", {"bills": bills})

from django.contrib.auth.models import User

def create_bill(request):
    User = get_user_model()   # ✅ important

    residents = User.objects.all()

    if request.method == "POST":
        resident_id = request.POST.get("resident")
        month = request.POST.get("month")
        amount = request.POST.get("amount")

        resident = User.objects.get(id=resident_id)

        MaintenanceBill.objects.create(
            resident=resident,
            month=month,
            amount=amount,
            status='pending'
        )

        return redirect('admin_bills')

    return render(request, 'create_bill.html', {
        'residents': residents
    })