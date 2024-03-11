from django.contrib.auth import authenticate, update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, ChangePasswordSerializer,ResetPasswordEmailSerializer
from .models import Researcher, Laboratory, Experiment, GroupExperiment, Animal, AnimalData, AnimalDataFields
from accounts.serializers import LaboratorySerializer, ExperimentSerializer , GroupExperimentSerializer, AnimalSerializer, AnimalDataSerializer, LaboratoryDetailSerializer, ExperimentDetailSerializer, GroupExperimentDetailSerializer, AnimalDetailSerializer, AnimalDataDetailSerializer, AnimalDataFieldsSerializer, AnimalDataFieldsDetailSerializer
from rest_framework import viewsets, permissions


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = Researcher.object.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key},status=status.HTTP_200_OK)
        
        return Response({'error':'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'success'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)
                return Response({'message': 'success'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([TokenAuthentication])
def get_user(request):
    if request.method == 'GET':
        content = {
            'username' : str(request.user.username),
            'email' : str(request.user.email),
            'role' : str(request.user.role),
            'accesslevel' : request.user.accessLevel
        }
    return Response(content)

class LaboratoryViewSet(viewsets.ModelViewSet):
  queryset = Laboratory.objects.all()
  permission_classes = [permissions.IsAuthenticated]

  def get_serializer_class(self):
        if self.action in ["list", "retrieve","get"]:
            return LaboratoryDetailSerializer
        return LaboratorySerializer

class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Experiment.objects.all()
        laboratory = self.request.query_params.get('laboratory')
        if laboratory is not None:
            queryset = queryset.filter(laboratory=laboratory)
        return queryset

    def get_serializer_class(self):
        if self.action in ["list", "retrieve", "get"]:
            return ExperimentDetailSerializer
        return ExperimentSerializer

class GroupExperimentViewSet(viewsets.ModelViewSet):
    queryset = GroupExperiment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = GroupExperiment.objects.all()
        experiment = self.request.query_params.get('experiment')
        if experiment is not None:
            queryset = queryset.filter(experiment=experiment)
        return queryset

    def get_serializer_class(self):
        if self.action in ["list", "retrieve", "get"]:
            return GroupExperimentDetailSerializer
        return GroupExperimentSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Animal.objects.all()
        group = self.request.query_params.get('group')
        if group is not None:
            queryset = queryset.filter(group=group)
        return queryset

    def get_serializer_class(self):
        if self.action in ["list", "retrieve", "get"]:
            return AnimalDetailSerializer
        return AnimalSerializer

class AnimalDataViewSet(viewsets.ModelViewSet):
    queryset = AnimalData.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve", "get"]:
            return AnimalDataDetailSerializer
        return AnimalDataSerializer
    
class AnimalDataFields(viewsets.ModelViewSet):
    queryset = AnimalDataFields.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get_serializer_class(self):
        if self.action in ["list", "retrieve" , "get"]:
            return AnimalDataFieldsDetailSerializer
        return AnimalDataFieldsSerializer