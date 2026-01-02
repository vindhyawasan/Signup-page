from django.contrib import admin
from .models import register

# admin.site.register(register)
@admin.register(register)
class registeradmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','username','email','password')
# Register your models here.
