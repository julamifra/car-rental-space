from django.shortcuts import render

# Create your views here.
def get_main(request):
    return render(request, 'main/main.html')
    # return HttpResponse("<h1> Hello! </h1><p>This is a paragraph!!</p>")