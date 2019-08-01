from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            "title":"Hello",
            "msg":"your data: ",
            "form": HelloForm()
        }

    def get(self, request):
        return render(request, "hello/index.html",self.params)

    def post(self, request):
        msg = "You are <b>" + request.POST["name"] + \
            "(" + request.POST["age"] + \
            ") </b>. <br> Your email address is <b>" + request.POST["mail"] + \
            "</b>."
        self.params["msg"] = msg
        self.params["form"] = HelloForm(request.POST)
        return render(request, "hello/index.html", self.params)




'''def index(request):
    params = {
        "title":"INDEX",
        "msg":"your data",
        "form":HelloForm(),
    }
    if(request.method == "POST"):
        params["msg"] = "名前：" + request.POST["name"] + \
            "<br>メール：" + request.POST["mail"] + \
            "<br>年齢：" + request.POST["age"]
        params["form"] = HelloForm(request.POST)
    return render(request, "hello/index.html",params)

def next(request):
    params = {
        "title":"INDEX",
        "msg":"What's your name?",
    }
    return render(request, "hello/index.html",params)


def form(request):
    msg = request.POST["msg"]
    params = {
        "title": "FORM",
        "msg": "Hello! " + msg,
    }
    return render(request, "hello/index.html", params)
'''
