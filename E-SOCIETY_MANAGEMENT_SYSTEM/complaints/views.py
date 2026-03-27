from django.shortcuts import render, redirect , get_object_or_404
from .forms import ComplaintForm
from .models import Complaint


def create_complaint(request):

    if request.method == "POST":

        form = ComplaintForm(request.POST)

        if form.is_valid():

            complaint = form.save(commit=False)
            complaint.resident = request.user
            complaint.save()

            return redirect('resident_dashboard')

    else:
        form = ComplaintForm()

    return render(request, "create_complaint.html", {"form": form})


def complaint_list(request):

    complaints = Complaint.objects.all()

    return render(request, "complaint_list.html", {"complaints": complaints})

def admin_complaints(request):

    complaints = Complaint.objects.all().order_by('-created_at')

    return render(request, "admin_complaints.html", {"complaints": complaints})

def update_complaint_status(request, complaint_id, status):

    complaint = get_object_or_404(Complaint, id=complaint_id)

    complaint.status = status
    complaint.save()

    return redirect("admin_complaints")