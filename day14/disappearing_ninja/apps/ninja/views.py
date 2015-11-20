from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ninja/index.html')

def color(request, color):
    context = {
        'color': color
    }
    return render(request, 'ninja/ninja.html', context)

def all(request):
    return render(request, 'ninja/all.html')
