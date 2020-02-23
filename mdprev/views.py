from django.shortcuts import render
from django.views.generic import TemplateView
from cloudlib import tashizan as tas
class mdPrev(TemplateView):
    def get(self, request):
        aaaa = tas.tashizan()
        print(aaaa.tasu(1,2))
        return render(request, "mdprev/index.html")




# Create your views here.
