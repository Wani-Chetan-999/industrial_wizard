from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('rag/', include('rag_engine.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('predictive/', include('predictive.urls')),
    path('reports/', include('reports.urls')), # Mounted Reports App
    path('', include('dashboard.urls')),
]