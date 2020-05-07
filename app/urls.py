from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # file listing page
    path('', views.FileListView.as_view(), name='file_list'),
    
    # 複数ファイル、モデルフォーム
    path('multi/upload/model/', views.multi_upload_with_model, name='multi_upload_with_model'),
]
