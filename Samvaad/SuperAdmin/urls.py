from django.urls import path
# from django.conf.urls.static import static
from SuperAdmin import views

app_name = "SuperAdmin"

urlpatterns = [
    path('addInstitute/',views.loadAddInstitutePage,name='loadAddInstitutePage'),
]