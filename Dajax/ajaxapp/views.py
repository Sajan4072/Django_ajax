from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    #creating an empty form
    
    form=StudentRegistration()
    stud=User.objects.all() 
    return render(request,'ajaxapp/home.html',{'form':form,'stu':stud})



# @csrf_exempt
def save_data(request):
    if request.method=="POST":
        form=StudentRegistration(request.POST)
        if form.is_valid():
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            usr=User(name=name, email=email ,password=password)
            usr.save()

            #after it is saved in DB the server shall send it back to ajax call so it can be rendered without refreshing
            stud=User.objects.values()
            student_data=list(stud)


            return JsonResponse({'status':'saved','student_data':student_data}) #this is also an api endpoint 
        else:
            return JsonResponse({'status':0})

