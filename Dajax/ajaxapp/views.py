from django.shortcuts import render
from . forms import StudentRegistration

# Create your views here.
def home(request):
    form=StudentRegistration() #creating an empty form
    return render(request,'home.html',{'form':form})

    


