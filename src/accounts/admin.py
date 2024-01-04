from django.contrib import admin
from .models import Researcher, Laboratory, Experiment, GroupExperiment, Animal, AnimalData

admin.site.register(Researcher)
admin.site.register(Laboratory)
admin.site.register(Experiment)
admin.site.register(GroupExperiment)
admin.site.register(Animal)
admin.site.register(AnimalData)



