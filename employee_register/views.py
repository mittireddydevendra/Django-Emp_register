from django.shortcuts import render,redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee
from django.urls import reverse

# Create your views here.
def handler404(request, exception):
   return render(request, '404handler.html')

def employee_list(request):
    context ={'employee_list':Employee.objects.all()}
    return render(request,"employee_register/employee_list.html",context)
    

def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)  
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
        return redirect('/employee/list')

# def employee_form(request, id=0):
#     if request.method == "GET":
#         if id == 0:
#             form = EmployeeForm()
#         else:
#             employee = get_object_or_404(Employee, pk=id)
#             form = EmployeeForm(instance=employee)
#         return render(request, "employee_register/employee_form.html", {'form': form})
#     else:
#         if id == 0:
#             form = EmployeeForm(request.POST)
#         else:
#             employee = get_object_or_404(Employee, pk=id)
#             form = EmployeeForm(request.POST, instance=employee)

#         if form.is_valid():
#             form.save()
#             return redirect(reverse('employee_list'))  # Use named URL instead of hardcoding

#     return render(request, "employee_register/employee_form.html", {'form': form})


def employee_delete(request,id):
    employee =Employee.objects.get(pk=id)  
    employee.delete()      
    return