from django.urls import path
from . import views

urlpatterns = [
    path('export/', views.generate_pdf_report, name='generate_pdf_report'),
]