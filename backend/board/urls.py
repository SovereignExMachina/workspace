from django.urls import path

from .views import Home, BoardDetail


app_name = 'board'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('board/<int:pk>', BoardDetail.as_view(), name='board_detail')
]
