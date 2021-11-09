from django.shortcuts import render, HttpResponse
from .models import Todo, ToMeet

# Create your views here.

def homepage(request):
    return render(request, 'index.html')


def test(request):
    todo_list = Todo.objects.all()
    return render(request, 'test.html', {'todo_list': todo_list})

def second(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, 'meeting.html', {'tomeet_list': tomeet_list})