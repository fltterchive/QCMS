from django.contrib import admin
from .models import User, Schedule, Penerimaan, Kalibrasi, Ukes, Service

# Register your models here.
admin.site.register(User)
admin.site.register(Schedule)
admin.site.register(Penerimaan)
admin.site.register(Kalibrasi)
admin.site.register(Ukes)
admin.site.register(Service)