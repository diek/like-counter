from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

from django.shortcuts import render


def home(request):
    return render(request, "home.html")  # This will render home.html template


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
