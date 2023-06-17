from django.urls import path
from .views import show_workspace


app_name = 'workspace'

urlpatterns = [
    path('', show_workspace),
]
