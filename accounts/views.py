from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from . models import Patient

def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    return render(request, 'accounts/dashboard.html')

def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form}) 

def patient_details_view(request):
    obj = Patient.objects.get(name = 'saish mhatre')
    context = {
        'name': obj.name,
        'age': obj.age,
        'mobile': obj.mobile,
        'sex': obj.sex,
        'address': obj.address,
        'occupation': obj.occupation,

        'contineous': obj.contineous,
        'type': obj.type,
        'aggravating': obj.aggravating,
        'relieving': obj.relieving,
        'duration': obj.duration,

        'disease': obj.disease,
        'recent_wt_loss': obj.recent_wt_loss,
        'breathing_pattern': obj.breathing_pattern,
        'heal_walking': obj.heal_walking,

        'morning_stiffness': obj.morning_stiffness,
        'numbness': obj.numbness,
        'mechanical_injury': obj.mechanical_injury,
        'mascular_weakness': obj.mascular_weakness,
        'sleeping_disturbance': obj.sleeping_disturbance,
        'mode_of_onset': obj.mode_of_onset,
        'claudication': obj.claudication
        }
    return render(request, "accounts/search.html", context)

def add_patient(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    mobile = request.POST.get("mobile")
    sex = request.POST.get("sex")
    address = request.POST.get("address")
    occupation = request.POST.get("occupation")
    patient = Patient(name=name, age=age, mobile=mobile, sex=sex, address=address, occupation=occupation)
    patient.save()

    print("patient record saved sucessfully")

    return render(request, "accounts/new.html")

def update_patient(request):
    return render(request, "accounts/update.html")

def delete_patient(request):
    return render(request, "accounts/delete.html")
