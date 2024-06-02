from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, EmodPageView, EventPageView, HandBookPageView, ResourcesPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('emod/', EmodPageView.as_view(), name='emod'),
    path('events/', EventPageView.as_view(), name='events'),
    path('handbook/', HandBookPageView.as_view(), name='handbook'),
    path('ressources/', ResourcesPageView.as_view(), name='ressources'),
]   