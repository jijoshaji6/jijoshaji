from django.contrib import admin

from schoolapp.models import store,Department,Course

# Register your models here.
admin.site.register(store)
admin.site.register(Department)
admin.site.register(Course)