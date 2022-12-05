from django.contrib import admin
from .models import Page, PageImage, PageTags

class PageImageInline(admin.StackedInline):
    model = PageImage
    extra = 1

class PageTagsInline(admin.StackedInline):
    model = PageTags
    extra = 1

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'body']})
    ]
    inlines = [PageImageInline, PageTagsInline]

# Register your models here.
admin.site.register(Page, PageAdmin)
