from django.contrib import admin
from .models import Grievance

@admin.register(Grievance)
class GrievanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'created_at')