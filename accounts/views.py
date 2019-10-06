from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from . models import Patient

def indexView(request):
    return render(request,'index.html')

@login_required
def dashboardView(request):
    return render(request,'accounts/dashboard.html')

def registerView(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form}) 

def patient_details_view(request):
    obj1 = Patient.objects.get(id=3)
  
    
    context ={
        'name': obj1.name,
        'age': obj1.age,
        'mobile': obj1.mobile,
        'sex': obj1.sex,
        'address': obj1.address,
        'occupation': obj1.occupation


   
    }
    return render(request,"accounts/search.html",context)



