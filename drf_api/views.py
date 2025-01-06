from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE
)

@api_view()
def test_view(request):
    return Response({"message": "Test successful!"})

@api_view()
def home_route(request):
    """
    API home route:
    - Returns a welcome message for the InstaPaws API.
    - Provides a simple endpoint to verify the API is running.
    """
    return Response({
        "message": "Hello! This is InstaPaws API"
    })

@api_view(['POST'])
def logout_route(request):
    """
    API logout route:
    - Clears JWT authentication and refresh cookies to log the user out.
    - Sets the cookies with an empty value and an expiration date in the past (1960).
    """
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1960 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1960 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response

def favicon(request):
    return HttpResponse(status=204)
