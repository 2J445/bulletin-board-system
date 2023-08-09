from .models import Article
from django.views import generic # Second add
from django.urls import path
from . import views
 
app_name = 'bbs'

# path('' で始まる行と path('<int:id>/' で始まる行を書き換える
urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:id>/', views.detail, name='detail'),
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # <int:id>から<int:pk>に変更されているので注意！
 
    # それ以外はこのまま
]