from django.shortcuts import render
from .models import Page

# Create your views here.
def page_list(request):
    pages = Page.objects.all()
    context = {"object_list": pages}
    return render(request, 'diary/index.html', context=context)