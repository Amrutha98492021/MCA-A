from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse 
from .models import EmployeeModel  
from .forms import EmployeeForm
from .models import StudentModel  
from .forms import StudentForm
from .models import FacaltyModel
from .forms import FacaltyForm
def insert_employee(request):
    context ={}
    ob_form = EmployeeForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_employee.html", context)  
def view_employee(request):
    ob=EmployeeModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_employee.html')
    return HttpResponse(temp.render(context,request))
def insert_student(request):
    context ={}
    ob_form = StudentForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_student.html", context)  
def view_student(request):
    ob=StudentModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_student.html')
    return HttpResponse(temp.render(context,request))
def insert_employee(request):
    context ={}
    ob_form = EmployeeForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_employee.html", context)  
def view_facalty(request):
    ob=FacaltyModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_facalty.html')
    return HttpResponse(temp.render(context,request))
def insert_facalty(request):
    context ={}
    ob_form = FacaltyForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_facalty.html", context)  

def delete_employee(request,pk):
    EmployeeModel.objects.get(id=pk) .delete()
    return render(request,"delete_employee.html")

def delete_student(request,pk):
    StudentModel.objects.get(id=pk) .delete()
    return render(request,"delete_student.html")
def  delete_facalty(request,pk):
    FacaltyModel.objects.get(id=pk) .delete()
    return render(request, "delete_facalty.html")

from django.shortcuts import get_object_or_404, redirect
def update_employee(request,pk):
    obe = get_object_or_404(EmployeeModel, id=pk)
    if request.method == 'POST':
        obf = EmployeeForm(request.POST, instance=obe)
        if obf.is_valid():
            obf.save()
        return redirect('view_employee')#, id=pk
    else:
        formdata=EmployeeForm(instance=obe)
    return render(request, "update_employee.html", {'form':formdata})

from django.shortcuts import get_object_or_404, redirect

def update_student(request,pk):
    obe = get_object_or_404(StudentModel, id=pk)
    if request.method == 'POST':
        obf = StudentForm(request.POST, instance=obe)
        if obf.is_valid():
            obf.save()
        return redirect('view_student')#, id=pk
    else:
        formdata=StudentForm(instance=obe)
    return render(request, "update_student.html", {'form':formdata})

from django.shortcuts import get_object_or_404, redirect

def update_facalty(request,pk):
    obe = get_object_or_404(FacaltyModel, id=pk)
    if request.method == 'POST':
        obf = FacaltyForm(request.POST, instance=obe)
        if obf.is_valid():
            obf.save()
        return redirect('view_facalty')#, id=pk
    else:
        formdata=FacaltyForm(instance=obe)
    return render(request, "update_facalty.html", {'form':formdata})



