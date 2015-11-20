from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'Emmett',
        'interest': 'Snowboarding',
        'language': 'Python'
    }
    return render(request, 'home/index.html', context)
