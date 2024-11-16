from django.shortcuts import render, redirect
from .forms import EmployeeForm


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            # TODO: сделать редирект для успешного заполнения формы
            return redirect('workers', pk=employee.pk)
    else:
        form = EmployeeForm()
    return render(request, 'workers/employee_form.html', {'form': form})
