from django.contrib import admin
from django.contrib.auth.models import User
from .models import ProjectType, ExardProduct, ProjectAssignment, AddUserSubmission

admin.site.register(ProjectType)
admin.site.register(ExardProduct)
admin.site.register(ProjectAssignment)
admin.site.register(AddUserSubmission)

# Optionally, to customize User admin, you can use:
# from django.contrib.auth.admin import UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
