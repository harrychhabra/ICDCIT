from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect, render
from Login.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from SuperAdmin import views as SuperAdminNameSpace
# Create your views here.

@csrf_protect
def user_login(request):
    template = loader.get_template('Login.html')
    if request.method == 'GET':
        return render(request,'Login.html',{})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        username = userTable.objects.filter(user_name = username)
        if len(username) != 1:
            return render(request,'Login.html',{'error_message':'true','message':'Invalid Input'})
            
        user = userLoginTable.objects.filter(password = password,user_name = username[0])
        
        if len(user) != 1:
            return render(request,'Login.html',{'error_message':'true','message':'Invalid Input'})
            
        if user[0].user_status == 'blocked':
            return render(request,'Login.html',{'error_message':'true','message': 'Account Blocked'})
        
        # Else load asked page
        # Ensured only one valid query will be processed
        return checkUserType(request,username[0])
# 
@csrf_protect
def checkUserType(request,user_object):
    if user_object.user_type == 'super_admin':
        return loadSuperAdmin(request,user_object)
    else:
        return HttpResponse("ADs")
        
@csrf_protect
def loadSuperAdmin(request,user_object):
    return SuperAdminNameSpace.loadSuperAdmin(request,user_object)
    
