from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:travel_id>/', views.booking_create_view, name='booking_create'),
    path('', views.booking_list_view, name='booking_list'),
    path('<int:booking_id>/', views.booking_detail_view, name='booking_detail'),
    path('<int:booking_id>/cancel/', views.booking_cancel_view, name='booking_cancel'),
]
