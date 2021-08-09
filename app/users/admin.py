from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users import models


admin.site.register(models.Doctor)
admin.site.register(models.Appointment)
admin.site.register(models.Patient)