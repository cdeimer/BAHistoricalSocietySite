from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class PageImage(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images')
    caption = models.CharField(max_length=500, default=None, blank=True, null=True)

    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="100" height="100" />' % (self.image))

    def __str__(self):
        return self.page.title + ": " + str(self.pk)

class PageTags(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='tags')
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.page.title + ": " + self.tag