from django.shortcuts import HttpResponse, render
from django.http import HttpResponseBadRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .email import validate_email

# Create your views here.

def index(request):
    return render(request, 'checkmail/index.html')


@api_view(['GET', 'POST'])
def mail_validation(request):
    if request.method == 'POST':
        email = request.POST['email']

        if not email:
            error_msg = {"msg":"email required"}
            return Response(status=400, data=error_msg)

        res = validate_email(email)

        if res['valid']:
            return Response(status=200, data=res)
        else:
            return Response(status=400, data=res)
