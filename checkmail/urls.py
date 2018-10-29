from django.urls import path
from . import views

app_name = 'checkmail'

urlpatterns = [
    path('', views.index, name='index'),
    path('validate/', views.validate_mail, name='validate_mail' )
]