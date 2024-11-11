from django.shortcuts import render,redirect
# Create your views here.
from django.shortcuts import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm
from django.contrib.auth.forms import UserCreationForm




def home(request):
    return render(request,'home.html',)



def signup_page(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})



def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
        else:print('error')
    else: form=BookingForm()   
            
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)

def contact(request):
    return render(request,'contact.html')

def department(request):
    dict_dept={
        'dept':Departments.objects.all()
                
    }
    return render(request,'department.html',dict_dept)
