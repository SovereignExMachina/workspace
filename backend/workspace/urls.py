from django.urls import path
from .views import show_workspace

urlpatterns = [
    path('', show_workspace),
]
