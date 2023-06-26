from django.urls import path
from .views import WorkSpaceView, WorkSpaceDetail, WorkSpaceCreate, ColumnCreate


app_name = 'workspace'

urlpatterns = [
    path('', WorkSpaceView.as_view(), name='home'),
    path('workspace/<int:pk>/', WorkSpaceDetail.as_view(), name='ws_detail'),
    path('workspace/create/', WorkSpaceCreate.as_view(), name='create_workspace'),
    path('workspace/<int:pk>/column/',
         ColumnCreate.as_view(), name='create_column'),
]
