from django.contrib import admin
from .models import Page, PageImage

class PageImageInline(admin.StackedInline):
    model = PageImage
    extra = 1

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'body']})
    ]
    inlines = [PageImageInline]

# Register your models here.
admin.site.register(Page, PageAdmin)
