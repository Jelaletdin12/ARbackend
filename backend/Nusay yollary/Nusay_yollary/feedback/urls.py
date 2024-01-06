# urls.py

from django.urls import path
from .views import feedback_view

urlpatterns = [
    path('api/feedback/', feedback_view, name='feedback'),
    # Diğer url pattern'leri...
]
