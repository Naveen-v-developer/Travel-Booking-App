from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_list_view, name='travel_list'),
    path('<int:pk>/', views.travel_detail_view, name='travel_detail'),
]
