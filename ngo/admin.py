from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'location')
    ordering = ('first_name',)
    search_fields = ('first_name','phone','email')


@admin.register(FundRaisingAgent)
class FundRaisingAgentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'id_number','email', 'phone', 'location')
    ordering = ('first_name',)
    search_fields = ('first_name','phone','email', 'id_number')


@admin.register(AnnualDonor)
class AnnualDonorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email', 'phone', 'location')
    ordering = ('first_name',)
    search_fields = ('first_name','phone','email', 'id_number')


@admin.register(GaleryImage)
class GaleryImageAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email')
    ordering = ('name',)
    search_fields = ('name', 'email')