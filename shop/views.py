from django.shortcuts import render
from .models import Item

def index(request):
    items = Item.objects.all()
    context = { 'inventory': items }
    return render(request, 'shop/index.html', context)