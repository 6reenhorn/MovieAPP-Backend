from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from .models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

def normalize_phone(phone):
    """ Convert phone number to a consistent format (e.g., +639123456789) """
    phone = phone.replace(" ", "").replace("-", "")  # Remove spaces or dashes
    if phone.startswith("+63"):  
        return phone  # Already in international format
    elif phone.startswith("09"):  
        return "+63" + phone[1:]  # Convert '09123456789' -> '+639123456789'
    elif phone.startswith("9") and len(phone) == 10:  
        return "+63" + phone  # Convert '9123456789' -> '+639123456789'
    return phone  # If it doesn't match, return as is

@csrf_exempt
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        fullName = request.data.get('fullName', None)
        email = request.data.get('email', None)
        phoneNumber = request.data.get('phoneNumber', None)
        password = request.data.get('password', None)

        if not fullName or not password or (not email and not phoneNumber):
            return JsonResponse({'error': 'Full name, password, and either email or phone number are required'}, status=400)
        
        if phoneNumber:
            phoneNumber = normalize_phone(phoneNumber)  # Normalize before saving
        
        user = User.objects.create_user(
            fullName=fullName,
            email=email,
            phoneNumber=phoneNumber,
            password=password 
        )
        return JsonResponse({'message': 'User registered successfully'}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
@api_view(['POST'])
def login_view(request):
    
    print("Raw request body:", request.body)  # Debugging
    print("Parsed request data:", request.data)  # Debugging

    if request.method == 'POST':
        identifier = request.data.get('identifier', None)
        password = request.data.get('password', None)

        print("Received identifier:", identifier)
        print("Received password:", password)

        if not identifier or not password:
            return JsonResponse({'error': 'Identifier (email or phone) and password are required'}, status=400)

        user = User.objects.filter(email=identifier).first()

        if not user:
            normalized_phone = normalize_phone(identifier)
            user = User.objects.filter(phoneNumber=normalized_phone).first()

        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'message': 'Login successful', 'token': token.key}, status=200)

        return JsonResponse({'error': 'Invalid credentials'}, status=401)
        
    return JsonResponse({'error': 'Invalid request method'}, status=405)