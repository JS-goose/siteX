from django.shortcuts import render

# Create your views here.
from Blog.models import account_information, blog_content, favorite_information

def index(request):
    users = account_information.object.all()
    return render(request,'html/index.html',{"users_all": users})

def About(request):
    return render(request,'html/About.html')


