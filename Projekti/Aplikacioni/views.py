from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def home (request):
     blogs=Blog.objects.all()
     context={"blogs":blogs}
     return render (request, "home.html", context)


def aboutus (request):
     reviews=Review.objects.all()
     context={"reviews":reviews}
     return render (request, "aboutus.html", context)

def activities (request):
     return render (request, "activities.html")

def contact (request):
     if request.method =='POST':
                   name=request.POST['txtName'] 
                   email=request.POST['txtEmail']
                   tel=request.POST['txtPhone']
                   mesazhi=request.POST['txtMsg']
                   Contact (contact_name=name,contact_message=mesazhi,contact_cel=tel,contact_email=email).save()
                   
                   
                   messages.success(request,'mesazhi u dergua')
                   return redirect('/') 

     return render (request, "contact.html")

def fullblog (request,id):
     fullblogs = Fullblog.objects.get(fullblog_id=id)
     context={"fullblogs":fullblogs}
     return render (request, "fullblog.html", context)

def packages (request):
     return render (request, "packages.html")

