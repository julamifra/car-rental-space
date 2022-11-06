from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_main(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'main/main.html', context)


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        # name = request.POST.get('item_name')
        # done = 'done' in request.POST
        # Item.objects.create(name=name, done=done)
        if form.is_valid():
            form.save()
            return redirect('get_main')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'main/add_item.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_main')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'main/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_main')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_main')
