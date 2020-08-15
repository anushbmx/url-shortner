from django.urls import path

from shortner import views
from shortner.views import ShortnerHome, ShortnerDetails, ShortnerRedirect

urlpatterns = [
    path('', ShortnerHome.as_view(), name='shortner.home'),
    path('d/<str:short_url>/', ShortnerDetails.as_view(), name='shortner.details'),

    path('r/<str:short_url>/', ShortnerRedirect.as_view(), name='shortner.redirect'),
]
