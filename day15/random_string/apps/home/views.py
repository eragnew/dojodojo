from django.shortcuts import render, redirect
import random, string

def get_random():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(14))

# Create your views here.
def index(request):
    if request.method == 'POST':
        if 'attempts' in request.session:
            request.session['attempts'] += 1
        else:
            request.session['attempts'] = 1
        request.session['random_string'] = get_random()
        return redirect('/')
    else:
        return render(request, 'home/index.html')
