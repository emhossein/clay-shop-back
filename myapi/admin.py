from django.contrib import admin
from .models import Items, ItemsMens, ItemsWomens

# Register your models here.
admin.site.register(Items)
admin.site.register(ItemsMens)
admin.site.register(ItemsWomens)
