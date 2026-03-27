from django.shortcuts import render, redirect
from .models import Announcement


def announcement_list(request):

    announcements = Announcement.objects.all().order_by('-created_at')

    return render(request, "announcement_list.html", {"announcements": announcements})


def create_announcement(request):

    if request.method == "POST":

        title = request.POST.get("title")

        message = request.POST.get("message")

        Announcement.objects.create(
            title=title,
            message=message,
            created_by=request.user
        )

        return redirect("announcement_list")

    return render(request, "create_announcement.html")