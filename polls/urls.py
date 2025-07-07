from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('detail/<int:pk>', views.project_detail, name='project_detail'),
    path('result/<int:pk>', views.project_result, name='project_result')
]