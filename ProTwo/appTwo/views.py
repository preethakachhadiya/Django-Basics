from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User

# Create your views here.

# def index(request):
#     return HttpResponse("<em>My Second Project</em>")
#
# def help(request):
#     help_dict = {'help_insert' : 'HELP PAGE'}
#     return render(request,'appTwo/help.html',context=help_dict)
def index(request):
    return HttpResponse("<h1>Welcome!</h1> <br> <h2>Go to /users to see the list of user information</h2>")

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request,'appTwo/users.html',context='user_dict')
