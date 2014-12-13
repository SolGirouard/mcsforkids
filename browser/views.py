from django.shortcuts import render
from .models import Item


def frontPage(request):
   items = Item.objects.all().order_by('minAge')
   return render(request, 'browser/frontPage.html', {'items': items})
