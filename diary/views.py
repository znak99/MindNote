from django.shortcuts import render
from .models import Page
from .forms import PageForm

# Create your views here.
def page_list(request):
    pages = Page.objects.all()
    context = {"object_list": pages}
    return render(request, 'diary/page_list.html', context=context)

def info(request):
    return render(request, 'diary/info.html')


def page_detail(request, page_id):
    page = Page.objects.get(id=page_id)
    context = {"object": page}
    return render(request, 'diary/page_detail.html', context=context)

def page_create(request):
    form = PageForm()
    return render(request, 'diary/page_form.html', {'form': form})