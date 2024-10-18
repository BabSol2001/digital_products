from django.contrib import admin

from .models import Category, Product, File
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title', 'is_enabled','created_time']
    list_filter = ['is_enabled', 'parent']
    search_fields = ['title']

class FileInLineAdmin(admin.StackedInline):
    model = File
    fields = ['title','file', 'is_enabled']
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enabled', 'created_time']
    list_filter = ['is_enabled']
    filter_horizontal = ['category']
    search_fields = ['title']
    inlines = [FileInLineAdmin]

