from django.contrib import admin

from .models import Employee
# Register your models here.
# admin.site.register(Employee)
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("fullname", "mobile","position")
    search_fields = ("fullname__startswith", )