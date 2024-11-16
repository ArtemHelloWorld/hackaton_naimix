from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            return redirect('workers:employees')
    else:
        form = EmployeeForm()
    return render(request, 'workers/employee_form.html', {'form': form})


# Отображение всех работников
def employees(request):
    template = 'workers/employees.html'
    employees = Employee.objects.filter(is_candidate='WR')
    context = {'employees': employees}
    return render(request, template, context)


# Отображение всех кандидатов
def candidates(request):
    template = 'workers/candidates.html'
    candidates = Employee.objects.filter(is_candidate='CA')
    context = {'candidates': candidates}
    return render(request, template, context)


# Удаление кандидата
def delete_candidate(request, candidate_id):
    candidate = get_object_or_404(Employee, id=candidate_id)
    candidate.delete()
    return redirect('workers:candidates')


# страничка с выбором - смотреть совместимость между 2мя или командой
def compatibility(request):
    pass

