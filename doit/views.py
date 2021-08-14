from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Todo

# Create your views here.
def home(request):
  todo_items = Todo.objects.all().order_by("-added_date")
  return render(request,'doit/index.html',{
    "todo_items":todo_items
  })
@csrf_exempt
def add_todo(request):
  added_date=timezone.now()
  todo= request.POST["todo"]
  created_obj = Todo.objects.create(added_date=added_date,text=todo)
  print(created_obj)
  return HttpResponseRedirect('/')

@csrf_exempt
def delete_todo(request, todo_id):
  Todo.objects.get(id=todo_id).delete()
  return HttpResponseRedirect('/')