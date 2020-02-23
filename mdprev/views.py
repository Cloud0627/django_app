from django.shortcuts import render
from django.views.generic import TemplateView 
class mdPrev(TemplateView):
    def get(self, request):
        return render(request, "mdprev/index.html")




# Create your views here.
