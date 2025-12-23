from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import Restaurant
from .serializers import RestaurantSerializer, UserSerializer

# CRUD complet pour Restaurant (GET, POST, PUT, DELETE automatique)
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [AllowAny]

# Inscription
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    
    data = {
        'email': email,
        'password': password,
        'username': email
    }
    
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        
        # ← AJOUTE CES 2 LIGNES pour sauvegarder le name
        user.first_name = name
        user.save()
        
        return Response({
            'id': user.id,
            'name': name,
            'email': user.email,
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            # Essaie de récupérer first_name, sinon username
            name = user.first_name if user.first_name else user.username
            
            return Response({
                'id': user.id,
                'name': name,  # ← Utilise first_name ou username
                'email': user.email,
            })
    except User.DoesNotExist:
        pass
    
    return Response(
        {'error': 'Invalid email or password'}, 
        status=status.HTTP_401_UNAUTHORIZED
    )