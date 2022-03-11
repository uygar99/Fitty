from django.contrib import admin
from .models import Workout, Status
from .models import Trainee
from .models import Trainer
admin.site.register(Workout)
admin.site.register(Trainee)
admin.site.register(Trainer)
admin.site.register(Status)

# Register your models here.
