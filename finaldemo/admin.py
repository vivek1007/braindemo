from django.contrib import admin
from .models import Contact,User
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
    list_filter = ['name']
    search_fields = ['subject']

admin.site.register(Contact,ContactAdmin)
admin.site.register(User)
