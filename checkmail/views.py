from rest_framework.decorators import api_view
from rest_framework.response import Response
from .email import validate_email


@api_view(['GET'])
def mail_validation(request, email):

    if not email:
        response_data = { 'message' : '메일을 입력해주세요.', 'valid':False }
        return Response(data=response_data, status=400, content_type='application/json')

    response_data = validate_email(email)
    return Response(status=response_data['status'], data=response_data)