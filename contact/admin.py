from django.contrib import admin
from .models import ContactList
from django.contrib.auth.models import Group

class ContactManage(admin.ModelAdmin):
    list_display = ('id','name','email','phone','cinfo','manager')
    list_editable = ('phone','cinfo')
    list_display_links = ('id','name')
    search_fields = ('name','email','phone','cinfo')
    list_filter = ('gender','datetime')
    list_per_page = 10
    

# Register your models here.
admin.site.register(ContactList,ContactManage)


admin.site.unregister(Group)

