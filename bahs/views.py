from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Page

# Create your views here.

def home(request):
    page_list = Page.objects.order_by('title')
    context = {
        'page_list': page_list,
    }
    return render(request, 'bahs/index.html', context)

def history(request):
    page_list = Page.objects.order_by('title')
    context = {
        'page_list': page_list,
    }
    return render(request, 'bahs/history.html', context)

def page_detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'bahs/page_detail.html', {'page': page})