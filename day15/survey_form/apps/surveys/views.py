from django.shortcuts import render, redirect
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, 'surveys/index.html')

def process(request):
    if request.method != 'POST':
        raise Http404('Invalid HTTP method!!! :(')
    if 'sub_count' in request.session:
        request.session['sub_count'] += 1
    else:
        request.session['sub_count'] = 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def result(request):
    return render(request, 'surveys/result.html')
