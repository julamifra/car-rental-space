from django.shortcuts import render
from .models import Item

# Create your views here.


def get_main(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'main/main.html', context)
    # return HttpResponse("<h1> Hello! </h1><p>This is a paragraph!!</p>")
