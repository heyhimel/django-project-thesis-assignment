from django.shortcuts import render, HttpResponse, redirect
from .models import * #importing all classes of model
from django.contrib import messages #message framework to show simple messages in html page
#used for providing feedback to users, such as confirmation, warnings, or error messages.


# Create your views here.


def home(request):
    return render(request, 'home.html')

def register(request):
    #data receiving from html file by post method
    if request.method == "POST":
        accType = request.POST.get('category')
        name = request.POST.get('nme')
        mail = request.POST.get('email')
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        
        #get_or_create holo jodi database userName already exist thake tahole new object create hobe na
        authenTable, created = userAuthenTable.objects.get_or_create(
            userName=uname, 
            defaults= {'userType':accType,'name':name,'gmail':mail,'passWord':passw}
            )
        

        if created:
            messages.success(request,"Registration succesfull, login please")#django message framework, it can pass data to redirect method
            return redirect('loginpage')

        else:
            messages.info(request,"Username already exist, please try another one")
            return redirect('registerpage')  
    
    return render(request, 'register.html')# {'checker':check,'message':msg})

def login(request):
    if request.method =="POST":
        accountType = request.POST.get('category')
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        loginDataRetrieve = userAuthenTable.objects.all()

        for eachdata in loginDataRetrieve:
            if eachdata.userName==uname and eachdata.passWord == passw and accountType == eachdata.userType:
                #session data is receiving for each user in per request session
                #this session data can easily access from html template
                request.session['user_data'] ={
                    'userType': eachdata.userType,
                    'userName': eachdata.userName,
                    'name': eachdata.name,
                    'gmail': eachdata.gmail,
                    'userId': eachdata.userId
                }
                if accountType=="supervisor":
                    return redirect('sup_homepage') #supervisor section redirect kora hobe
                
                # if accountType == 'student':
                #     return redirect('')
                
                # if accountType == 'cordinator':
                #     return redirect('')
            
            
        return render(request, 'login.html',{'errorMsg':"UserName or Password Invalid"})

    return render(request, 'login.html')
