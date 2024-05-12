from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # представления поста
    #path('', views.tool_list, name='tool_list'),
    path('', views.ToolListView.as_view(), name='tool_list'),
    path('<int:id>/', views.tool_detail, name='tool_detail'),
]
