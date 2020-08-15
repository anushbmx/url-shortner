from django.urls import path

from shortner import views

urlpatterns = [
    path('', views.home, name='shortner.home'),
    path('success', views.success, name='shortner.success'),
]
