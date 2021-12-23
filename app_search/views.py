from django.shortcuts import render, redirect
from .models import *
import datetime
import random
from django.contrib.auth import login, authenticate
# Create your views here.


def home(request):
    print(request.POST)
    user = User.objects.get(user=f'user1')
    if user.key == True:
        if request.method == 'POST':
            if 'search' in request.POST:
                question = request.POST['search']
                if len(question) > 2:
                    filter_question = Question.objects.filter(question__contains=question)
                    filter_answer = Question.objects.filter(answer__contains=question)
                    if filter_question.exists():
                        print('fileer')
                        return render(request, 'home.html', {'filter': filter_question})
                    elif filter_answer.exists():
                        return render(request, 'home.html', {'filter': filter_answer})
                    else:
                        return render(request, 'home.html', {'null': 'null'})
                else:
                    return render(request, 'home.html', {'null': 'null'})
        return render(request, 'home.html')
    else:
        return redirect('/')


def log_in(request):
    user = User.objects.get(user='user1')
    if len(User.objects.filter(user='user1')) == 0:
        create_user = User.objects.create(
            user=f'user{2}',
            promo_cod=str(random.randint(100000, 999999))
        )
        create_user.save()
    elif user.promo_cod == '':
        user.promo_cod = str(random.randint(100000, 999999))
        user.save()
    if user.key == False:
        if request.method == 'POST':
            print(user.key)
            if 'key' in request.POST:
                print('key')
                key = request.POST['key']
                if key == user.promo_cod:
                    user.key = True
                    user.save()
                return redirect('/home')
        elif request.method == 'GET':
            return render(request, 'login.html', {'user_key': user.promo_cod[::-1]})
    else:
        return redirect('/home')


def close_url(request):
    user = User.objects.get(user='user1')
    user.key = False
    user.promo_cod = ''
    user.save()
    return redirect('/')