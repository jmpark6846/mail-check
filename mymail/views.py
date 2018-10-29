from django.shortcuts import HttpResponse, render
from django.http import HttpResponseBadRequest
from .email import validate_email

# Create your views here.

def index(request):
    return render(request, 'index.html')

def validate_mail(request):
    if request.method == 'POST':
        email = request.POST['email']
        res = validate_email(email)

        if res.valid:
            return HttpResponse()

    return HttpResponseBadRequest('nope')

