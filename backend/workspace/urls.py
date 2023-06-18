from django.urls import path
from .views import show_workspace, get_workspace


app_name = 'workspace'

urlpatterns = [
    path('', show_workspace, name='home'),
    path('workspace/<int:ws_id>', get_workspace, name='ws_detail'),
]
