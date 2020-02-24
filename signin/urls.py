from django.urls import path
from .views import SigninClass

urlpatterns = [
    path(r'', SigninClass.as_view(), name="index"),
    path('activation.html', SigninClass.activation, name="activation"),
    #path('form', views.form, name="form"),
]
