from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import GameProduct
# Create your views here.

temp = {'temp': [1,2,3,4,5]}

def index(request):
    games = GameProduct.objects
    return render(request, 'main.html', {'games': games})


def details(request, game_id):
    game_detail = get_object_or_404(GameProduct, pk=game_id)
    return render(request, 'details.html', {'game_data': game_detail})


def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if len(password) >= 8:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists!')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
        else:
            messages.info(request, 'Password should be 8 characters long!')
            return redirect('signup')

    else:
        messages.info(request, '')
        return render(request, 'signup.html')