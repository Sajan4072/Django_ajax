from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def home(request):
    #creating an empty form
    
    form=StudentRegistration()
    stud=User.objects.all() 
    return render(request,'ajaxapp/home.html',{'form':form,'stu':stud})




