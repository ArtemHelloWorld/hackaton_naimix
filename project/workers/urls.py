import django.urls
import workers.views

app_name = 'workers'

urlpatterns = [
    django.urls.path(
        'questionnaire/',
        workers.views.employee_create,
        name="questionnaire",
    ),
    django.urls.path(
        'employees/',
        workers.views.employees,
        name="employees",
    ),
    django.urls.path(
        'candidates/',
        workers.views.candidates,
        name="candidates",
    ),
    django.urls.path(
        'delete_candidate/<int:candidate_id>/',
        workers.views.delete_candidate,
        name='delete_candidate'),

]
