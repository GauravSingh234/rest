from django.contrib import admin
from .models import students

# @admin.register(index)
class enquiryadmin(admin.ModelAdmin):
    list_display = ('Name','fathers_name','mothers_name', 'age', 'address', 'pincode', 'mobile')
    search_fields = ('Name', 'age', 'mobile')
    list_filter = ('Name', 'age', 'mobile')


admin.site.register(students, enquiryadmin)
