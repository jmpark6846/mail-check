from django.shortcuts import render
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.response import Response
from .email import validate_email


def index(request):
    return render(request, 'checkmail/index.html')

@api_view(['GET'])
@throttle_classes([AnonRateThrottle, UserRateThrottle])
def mail_validation(request, email):

    if not email:
        response_data = { 'message' : '메일을 입력해주세요.', 'valid':False }
        return Response(data=response_data, status=400, content_type='application/json')

    response_data = validate_email(email)
    return Response(status=response_data['status'], data=response_data)