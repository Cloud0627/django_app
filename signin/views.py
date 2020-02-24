from django.shortcuts import render
from django.views.generic import TemplateView

class SigninClass(TemplateView):
    def get(self, request):
        print(request)
        return render(request, "signin/signup.html")

    def activation(request):
        return render(request, "signin/activation.html")

# Create your views here.
