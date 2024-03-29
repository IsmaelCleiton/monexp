from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.db import models

class Laboratory(models.Model):
    id = models.BigAutoField(primary_key= True,unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return  self.name

class Experiment(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
class AnimalDataFields(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    informations_fields = models.JSONField(default=dict)
    
    def __str__(self):
        return 'informations_fields: {self.information_fields};'

class GroupExperiment(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    animal_data_fields = models.ForeignKey(AnimalDataFields, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Animal(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    group = models.ForeignKey(GroupExperiment, on_delete=models.CASCADE)
    identification = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    
    def __str__(self):
        return self.identification

class AnimalData(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True);
    informations = models.JSONField(default=dict);

    def __str__(self):
        return 'identification: {self.animal.identification}; informations: {self.informations};'
    

class Researcher(AbstractUser):
    id = models.BigAutoField(primary_key=True,unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=40,blank=True,null=True)
    accessLevel = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.username
    

