from django.urls import path
from django.conf.urls.static import static
from InstituteAdmin import views

app_name = "InstituteAdmin"

urlpatterns = [
    # path('addInstitute/',views.loadAddInstitutePage,name='loadAddInstitutePage'),
    path('',views.loadInstitutePage,name='loadInstitutePage'),
    path('adduser/',views.loadAddUserPage,name='loadAddUserPage'),
]