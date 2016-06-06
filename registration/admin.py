from django.contrib import admin

# Register your models here.
from registration.models import *
class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User,UserAdmin)

class ChocolateAdmin(admin.ModelAdmin):
    pass
admin.site.register(Chocolate,ChocolateAdmin)

