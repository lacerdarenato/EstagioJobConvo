from django.contrib import admin
from .models import vagas

class VagasAdmin(admin.ModelAdmin):
    list_display = ['name', 'faixaSalarial', 'escolaridadeMinima']
    search_fields = ['name']

admin.site.register(vagas, VagasAdmin)