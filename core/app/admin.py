from django.contrib import admin

from .models import Branch, Contact, Category, Course

admin.site.register(Branch)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Course)

