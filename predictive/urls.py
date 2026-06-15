from django.urls import path
from . import views

urlpatterns = [
    path('', views.live_ml_diagnostics, name='live_ml_diagnostics'),
]