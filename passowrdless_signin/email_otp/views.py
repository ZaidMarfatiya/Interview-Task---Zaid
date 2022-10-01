import random
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import send_email
from .models import Customer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            username = request.data.get('username')
            email = request.data.get('email')

            User.objects.create(username=username, email=email)
            return Response({"Msg": "User register successfully."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignInView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            email = request.data.get('email')

            if User.objects.filter(email=email).exists():
                username = User.objects.get(email=email).username
                user = User.objects.get(username=username)
                otp = random.randrange(100000, 999999)
                Customer.objects.create(user=user, otp_code=otp)
                request.session['username'] = username
                body = f"Dear {username}, your OTP for login is {otp}. Use this OTP to validate your login."
                data = {
                    'subject': 'OTP request',
                    'body': body,
                    'to_email': email
                }
                send_email(data)
                return Response({"Msg": "Email sent successfully."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"Msg": "Email doesn't exists. Kindly register."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OTPVerifyView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        try:
            username = request.session['username']
            otp = request.POST.get('otp')
            user = User.objects.filter(username = username).first()
            customer = Customer.objects.get(user=user)
            if int(otp) == customer.otp_code:
                refresh = RefreshToken.for_user(user)
                return Response({"username": f"{username} successfully login", 'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_201_CREATED)
            else:
                return Response({"Error": "Wrong OTP"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def add(a, b):
    sum = a + b
    return sum

def sub(a, b):
    s = a - b
    return s
        
class UserInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        return Response({"username": user.username, "email": user.email}, status=status.HTTP_200_OK)
