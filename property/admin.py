from django.contrib import admin
from .models import Flat, Complaint, Owner

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ["created_at",]
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by', 'owners',)

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat','user')

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owner_flats',)
    list_display = ('owner', 'owner_pure_phone',)
    search_fields = ('owner', 'owner_pure_phone',)

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)