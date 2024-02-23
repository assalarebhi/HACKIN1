
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .models import Child

class SignUp(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        if not username or not email or not password:
            return Response({'error': 'Veuillez fournir un nom d\'utilisateur, un email et un mot de passe.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Ce nom d\'utilisateur existe déjà.'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({'message': 'Inscription réussie.'}, status=status.HTTP_201_CREATED)

class SignIn(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': 'Connexion réussie.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Nom d\'utilisateur ou mot de passe incorrect.'}, status=status.HTTP_401_UNAUTHORIZED)


class ChildInformation(APIView):
    def post(self, request):
        name = request.data.get('name')
        age = request.data.get('age')
        school_level = request.data.get('school_level')
        health_issue = request.data.get('health_issue')
        description = request.data.get('description')

        # Enregistrer les informations de l'enfant dans la base de données
        child = Child.objects.create(
            name=name,
            age=age,
            school_level=school_level,
            health_issue=health_issue,
            description=description
        )

        return Response({'message': 'Informations sur l\'enfant enregistrées avec succès.'}, status=status.HTTP_201_CREATED)
