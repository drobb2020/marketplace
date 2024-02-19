from django.contrib.auth import logout
from django.shortcuts import redirect, render

from item.models import Category, Item


from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {"items": items, "categories": categories}
    return render(request, "core/index.html", context)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:home")
    else:
        form = SignupForm()

    context = {"form": form}
    return render(request, "core/signup.html", context)


def logout_view(request):
    logout(request)
    return redirect("core:home")


def contact(request):
    context = {}
    return render(request, "core/contact.html", context)


def about(request):
    context = {}
    return render(request, "core/about.html", context)


def privacy(request):
    context = {}
    return render(request, "core/privacy.html", context)


def terms(request):
    context = {}
    return render(request, "core/terms_and_conditions.html", context)
