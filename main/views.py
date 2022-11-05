from django.shortcuts import render, redirect
from .models import Item

# Create your views here.


def get_main(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'main/main.html', context)


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_main')
    return render(request, 'main/add_item.html')
