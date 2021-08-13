from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request,'doit/index.html')

def add_todo(request):
  print(request)