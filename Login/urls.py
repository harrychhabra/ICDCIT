from django.urls import path
from Login import views


app_name = "Login"

urlpatterns = [
    path(r'',views.user_login,name='user_login'),
]
