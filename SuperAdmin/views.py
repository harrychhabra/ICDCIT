from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from Login import models as LoginModels

# Create your views here.
def loadSuperAdmin(request,user_object):
    username = user_object.user_name
    first_name = user_object.first_name
    last_name = user_object.last_name
    organization = user_object.organization
    profile_pic = user_object.profile_pic
    
    data = {
        'username':username,
        'first_name':first_name,
        'last_name': last_name,
        'organization': organization,
        'profile_pic': profile_pic,
    }
    return render(request,'SuperAdmin.html',{'data':data})

@csrf_protect
def loadAddInstitutePage(request):
    if request.method == 'GET':
        return redirect(reverse('Login:user_login'))
    if request.method == 'POST':
        # if super admin wants to add, so no data will be provided
        # if data is present
        if request.POST.get('password'):
            data = addInstitute(request)
            return render(request,'addInstitute.html',{'data':data})
        
        # data is not present
        data = {}
        return render(request,'addInstitute.html',{'data':data})

@csrf_protect
def addInstitute(request):
    print("HERE")
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        institute_name = request.POST.get('institute_name')
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        
        # Check if user_name already existed or not
        user_detail_from_table = LoginModels.userTable.objects.filter(user_name = user_name)
        data = {
            'error_message':'',
            'message':'',
        }
        # If present
        if len(user_detail_from_table) != 0:
            data['error_message'] = 'true'
            data['message'] = 'User Name already exist'
            return data
        
        #user_name present
        # add details to userTable
        # first_name,last_name,institute_name,user_name to userTable
        # password to userLoginTable
        user_detail_from_table = LoginModels.userTable()
        user_detail_from_table.user_name = user_name
        user_detail_from_table.first_name = first_name
        user_detail_from_table.last_name = last_name
        user_detail_from_table.user_type = 'institute_user'
        user_detail_from_table.organization = institute_name
        user_detail_from_table.save()
        user_Login_table = LoginModels.userLoginTable()
        user_Login_table.user_name = user_detail_from_table
        user_Login_table.password = password
        user_Login_table.user_status = 'active'
        user_Login_table.save()
        data['error_message'] = 'true'
        data['message'] = 'Institute User Added'
        return data