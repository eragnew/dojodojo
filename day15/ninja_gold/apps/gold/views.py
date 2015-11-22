from django.shortcuts import render, redirect
from django.http import Http404
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = ['You started the game!']
    return render(request, 'gold/index.html')

def process(request):
    if request.method != 'POST':
        raise Http404('Invalid HTTP method!')
    if request.POST['building'] == 'farm':
        new_gold = random.randrange(10,21)
        msg = 'Earned %d from the farm!' % new_gold
    elif request.POST['building'] == 'cave':
        new_gold = random.randrange(5,11)
        msg = 'Earned %d from the cave!' % new_gold
    elif request.POST['building'] == 'house':
        new_gold = random.randrange(2,6)
        msg = 'Earned %d from the house!' % new_gold
    elif request.POST['building'] == 'casino':
        new_gold = random.randrange(-50,51)
        if new_gold < 0:
            msg = 'You lost %d at the casino :(' % new_gold
        else:
            msg = 'You earned %d at the casino :)' % new_gold
    request.session['gold'] += new_gold
    request.session['activities'].append(msg)
    return redirect('/')
