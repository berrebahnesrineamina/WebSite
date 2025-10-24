from django.contrib import admin
from .models import Client, PendingClient, Service

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'nin_number', 'phone_number', 'state', 'gender')
    list_filter = ('state', 'gender')
    search_fields = ('full_name', 'email', 'nin_number', 'phone_number')
    ordering = ('full_name',)

@admin.register(PendingClient)
class PendingClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'code', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('full_name', 'email')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_type', 'status', 'created_at')
    list_filter = ('service_type', 'status', 'created_at')
    search_fields = ('user__full_name', 'user__email', 'service_type')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
