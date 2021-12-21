from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    if request.method == 'POST':
        question = request.POST['serach']
        filters = Question.objects.filter(question__contains=question)
        print(filters)
        if filters.exists():
            return render(request, 'home.html', {'filter': filters})
        else:
            return render(request, 'home.html', {'null': 'null'})
    return render(request, 'home.html')