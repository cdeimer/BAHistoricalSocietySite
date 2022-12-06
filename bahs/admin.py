from django.contrib import admin
from .models import Page, PageImage, PageTag

class PageImageInline(admin.StackedInline):
    model = PageImage
    extra = 1

class PageTagInline(admin.StackedInline):
    model = PageTag
    extra = 1

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'body', 'page_type', 'related_pages', 'attribution']})
    ]
    inlines = [PageImageInline, PageTagInline]

# Register your models here.
admin.site.register(Page, PageAdmin)
