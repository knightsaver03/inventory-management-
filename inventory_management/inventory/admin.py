'from django.contrib import admin
from django.contrib.auth.models import User
from .models import ProjectType, ExardProduct, AddUser, ExcelData

class AddUserAdmin(admin.ModelAdmin):
	list_display = ('username', 'password', 'created_at')


class ExhardProductAdmin(admin.ModelAdmin):
	list_display = ('project_type','alpha_number','quantity')

admin.site.register(ProjectType)
admin.site.register(ExardProduct, ExhardProductAdmin)
admin.site.register(AddUser, AddUserAdmin)
admin.site.register(ExcelData)

# Optionally, to customize User admin, you can use:
# from django.contrib.auth.admin import UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)




'