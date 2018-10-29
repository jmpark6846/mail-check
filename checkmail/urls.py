from django.urls import path
from . import views

app_name = 'checkmail'

urlpatterns = [
    path('', views.index, name='index'),
    path('validate/', views.mail_validation, name='validate_mail' )
]