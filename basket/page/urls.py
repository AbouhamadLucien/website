from django.urls import path
from .views import signup
from .views import home

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', home, name='home'),
]