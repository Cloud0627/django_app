from django.urls import path
from .views import HelloView

urlpatterns = [
    path(r'', HelloView.as_view(), name="index"),
    #path('next', views.next, name="next"),
    #path('form', views.form, name="form"),
]
