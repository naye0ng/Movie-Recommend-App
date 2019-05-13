from django.shortcuts import render

# Create your views here.
def users(request):
    return render(request,'admin/users.html')

def movies(request):
    pass