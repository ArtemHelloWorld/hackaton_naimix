import django.urls
import workers.views

app_name = 'workers'

urlpatterns = [
    django.urls.path(
        'questionnaire/',
        workers.views.employee_create,
        name="questionnaire",
    )
]
