from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Worker


@login_required
def index(request):
    """View function for the home page of the site."""

    num_workers = Worker.objects.count()
    # num_cars = Car.objects.count()
    # num_manufacturers = Manufacturer.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_workers": num_workers,
        # "num_cars": num_cars,
        # "num_manufacturers": num_manufacturers,
        "num_visits": num_visits + 1,
    }

    return render(request, "task_manager/index.html", context=context)