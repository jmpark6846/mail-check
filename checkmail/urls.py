from django.urls import path
from . import views

app_name = 'checkmail'

urlpatterns = [
    path('<str:email>', views.mail_validation, name='validate_mail' )
]