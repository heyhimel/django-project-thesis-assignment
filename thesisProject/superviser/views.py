from django.shortcuts import render, HttpResponse, redirect
from .models import * #importing all classes of model
from home_login_signup.models import*


def sup_home(request):
    user_data = request.session.get('user_data', None)
    print(user_data.get('userId'))
    return render(request, 'sup_home.html',{'user_data':user_data})

def createProject(request):
    if request.method == "POST":
        projName = request.POST.get("project_name")
        projDetails = request.POST.get("project_details")
        stDate = request.POST.get("start_date")
        endDate = request.POST.get("end_date")
        maxStu = request.POST.get("max_students")
        chkBox = request.POST.get("checkPublish")
        if chkBox == "on":
            chkBox= True
        else:
            chkBox = False

        
        # session data theke userId collect kore supervisor data model a pass korte hobe
        user_data = request.session.get("user_data", None)
        
        
        #ekahane data type valo kore kheyal kore assign korte hobe
        #foreign key te data assign na kore full object ta assign korte hoy
        objForFk =userAuthenTable.objects.get(userId = user_data.get('userId'))

        print(objForFk)
        obj = supCreateProject(supProjId =objForFk,projName=projName, projDetails=projDetails,startDate=stDate,endDate=endDate,approveOrNot=chkBox,highestStudents=maxStu)
        obj.save()
        
        
        return redirect("my_project_list_page")
    return render(request,'create_project.html')

def myProject(request):
    user_data = request.session.get("user_data", None)
    return render(request, 'my_project.html',{"user_data": user_data})
