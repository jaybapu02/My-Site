from django.contrib import admin
from .models import Contact

# Register your model
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "desc")  # columns in admin
    search_fields = ("name", "email", "phone")  # search bar
    list_filter = ("desc",)  # filter by date