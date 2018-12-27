from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from Login import models as LoginModels
# Create your views here.

def loadInstitutePage(request):
    # Temporary pick user
    user_details = LoginModels.userTable.objects.filter(user_type = 'institute_admin')
    username = user_details[0].user_name
    first_name = user_details[0].first_name
    last_name = user_details[0].last_name
    organization = user_details[0].organization
    profile_pic = user_details[0].profile_pic
    data = {
        'username' : username,
        'first_name' : first_name,
        'last_name' : last_name,
        'organization' : organization,
        'profile_pic' : profile_pic,
    }
    return render(request,'InstituteAdmin.html',{'data':data})

def loadAddUserPage(request):
    return render(request,'addUser.html',{})