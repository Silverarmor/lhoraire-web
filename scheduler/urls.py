from django.urls import path

from . import views

app_name = 'scheduler'

urlpatterns = [
    path('create', views.get_name, name='create'),
    path('schedule', views.schedule, name='schedule'),
]
