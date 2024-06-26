from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    def embedding_display(self, obj):
        if obj.embedding:
            return ', '.join(str(item) for item in obj.embedding.values())
        else:
            return '-'