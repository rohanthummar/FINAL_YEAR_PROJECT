from django.shortcuts import render, redirect,get_object_or_404
from .forms import VisitorForm
from .models import Visitor


def create_visitor(request):

    if request.method == "POST":

        form = VisitorForm(request.POST)

        if form.is_valid():

            visitor = form.save(commit=False)
            visitor.resident = request.user
            visitor.save()

            return redirect('resident_dashboard')

    else:

        form = VisitorForm()

    return render(request, 'create_visitor.html', {'form': form})


def visitor_list(request):

    visitors = Visitor.objects.all()

    return render(request, 'visitor_list.html', {'visitors': visitors})

def approve_visitor(request, visitor_id):

    visitor = get_object_or_404(Visitor, id=visitor_id)

    visitor.status = "approved"
    visitor.save()

    return redirect("security_dashboard")


def reject_visitor(request, visitor_id):

    visitor = get_object_or_404(Visitor, id=visitor_id)

    visitor.status = "rejected"
    visitor.save()

    return redirect("security_dashboard")

def security_visitors(request):

    visitors = Visitor.objects.filter(status="pending")

    return render(request, "security_visitors.html", {"visitors": visitors})