from django.contrib import admin
from .models import ToDoList, Item, contactForm, postForm, upForm, Category, Food
# Register your models here.

admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(contactForm)
admin.site.register(Category)

""" get dt from dtb"""
admin.site.register(postForm)
""" upload """
admin.site.register(upForm)
"""API"""
admin.site.register(Food)
