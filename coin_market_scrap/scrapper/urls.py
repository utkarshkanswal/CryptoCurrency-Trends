# from django.conf.urls import url
from django.urls import path, include
from .views import (
    ScrappedDataListApiView,
)

urlpatterns = [
    path('api', ScrappedDataListApiView.as_view()),
]