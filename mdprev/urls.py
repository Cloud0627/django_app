from django.urls import path
from .views import mdPrev

urlpatterns = [
    path(r'', mdPrev.as_view(), name="index"),
    #path('next', views.next, name="next"),
    #path('form', views.form, name="form"),
]
