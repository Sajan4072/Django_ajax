from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def home(request):
    #creating an empty form
    
    form=StudentRegistration() 
    return render(request,'ajaxapp/home.html',{'form':form})




