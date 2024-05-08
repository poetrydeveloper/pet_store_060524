from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # представления поста
    path('', views.tool_list, name='post_list'),
    path('<int:id>/', views.tool_detail, name='post_detail'),
]
