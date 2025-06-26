from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('new/', include('new.urls'))
]