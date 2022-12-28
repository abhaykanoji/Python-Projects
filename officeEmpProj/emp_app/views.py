# pylint: disable=import-error
from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from django.db.models import Q
# Create your views here.


def index(request):
    return render(request, "index.html")


def all_employee(request):
    emps = Employee.objects.all()
    context = {
        "emps": emps
    }
    print(context)
    return render(request, "all_employee.html", context)


def add_employee(request):
    # if request.method == "POST":
    #     first_name = request.POST["first_name"]
    #     last_name = request.POST["last_name"]
    #     salary = int(request.POST["salary"])
    #     bonus = int(request.POST["bonus"])
    #     phone = int(request.POST["phone"])
    #     department = int(request.POST["department"])
    #     role = int(request.POST["role"])
    #     new_emp = Employee(first_name= first_name, last_name= last_name, salary= salary, bonus= bonus, phone= phone, department_id= department, role_id= role)
    #     new_emp.save()
    #     return HttpResponse("data_added")
    # elif request.method == "GET":
    #     return render(request, "add_employee.html")
    # else:
    #     return HttpResponse("some error occur")
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        department = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary,
                           bonus=bonus, phone=phone, department_id=department, role_id=role)
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method == 'GET':
        return render(request, 'add_employee.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")


def remove_employee(request, emp_id=0):
    if emp_id:
        try:
            emp_remove= Employee.objects.get(id=emp_id)
            emp_remove.delete()
            return HttpResponse("removed")
        except:
            return HttpResponse("error")
    emps= Employee.objects.all()
    context = {
        "emps" : emps
    }
    return render(request, "remove_employee.html", context)


def filter_employee(request):
    if request.method == "POST":
        name= request.POST["name"]
        department= request.POST["department"]
        role= request.POST["role"]
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if department:
            emps = emps.filter(dept__name__icontains = department)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'all_employee.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_employee.html')
    else:
        return HttpResponse('An Exception Occurred')


    # return render(request, "filter_employee.html")
