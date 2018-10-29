from django.urls import path
from . import views

app_name = 'checkmail'

urlpatterns = [
    path('validate/', views.validate_mail, name='validate_mail' )
]