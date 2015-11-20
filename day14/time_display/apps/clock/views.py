from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    context = {
        'current_time': datetime.datetime.now().strftime('%b %d, %Y %I:%M %p')
    }
    return render(request, 'clock/index.html', context)
