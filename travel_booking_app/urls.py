from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('travels/', include(('travels.urls', 'travels'), namespace='travels')),
    path('bookings/', include(('bookings.urls', 'bookings'), namespace='bookings')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
