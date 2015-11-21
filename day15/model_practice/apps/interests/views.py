from django.shortcuts import render
from models import Interest, User
# Create your views here.

def index(request):
    return render(request, 'interests/index.html')

def all(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'interests/interests.html', context)

def one(request, user_id):
    user = User.objects.get(id=user_id)
    context = {'user': user}
    return render(request, 'interests/interest.html', context)
