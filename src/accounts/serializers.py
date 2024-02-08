from rest_framework import serializers
from .models import Researcher, Laboratory, Experiment, GroupExperiment, Animal, AnimalData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Researcher
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        user = Researcher(username = validated_data['username'],email=validated_data['email']
                          )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = '__all__'

class LaboratoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = '__all__'
        depth = 1

class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = '__all__'

class ExperimentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = '__all__'
        depth = 1

class GroupExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupExperiment
        fields = '__all__'

class GroupExperimentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupExperiment
        fields = '__all__'
        depth = 1

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class AnimalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
        depth = 1

class AnimalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalData
        fields = '__all__'

class AnimalDataDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalData
        fields = '__all__'
        depth = 1


