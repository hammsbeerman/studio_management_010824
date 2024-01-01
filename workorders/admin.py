from django.contrib import admin

from .models import Workorder, ItemCategory, Category, WorkorderItem


class WorkorderAdmin(admin.ModelAdmin):
    fields = ['customer', 'workorder', 'internal_company', 'description', 'deadline', 'budget', 'quoted_price', 'original_order']


admin.site.register(Workorder, WorkorderAdmin)



class ItemCategoryAdmin(admin.ModelAdmin):
   #extra = 0
   # readonly_fields = ['created', 'updated']
    fields = ['workorder', 'description', 'category', 'internal_company']
    ordering = ('-workorder',)

admin.site.register(ItemCategory, ItemCategoryAdmin)


#class ItemCategoryAdmin(admin.ModelAdmin):
#    fields = ['workorder', 'description', 'category', 'internal_company']

admin.site.register(Category)

admin.site.register(WorkorderItem)
