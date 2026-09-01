from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Subjects.models import Subjects
from Topics.models import Topics


def signup(request):
    context={}
    try:
        if(request.method=="POST"):
            username=request.POST.get("username")
            password=request.POST.get("pwd")

            
            User.objects.create_user(
                            username=username,
                            password=password
                        )

            return redirect("deshboard")        
        else:
            print("not hello")
    except Exception as e:
        context={
            "error":"Already have an account to this username"
        }

    return render(request,"signup.html",context)


def login_user(request):
    context={
        "data":"yes"
    }
    try:
        if(request.method=="POST"):
            username=request.POST.get("username")
            password=request.POST.get("pwd")

            user=authenticate(
                username=username,
                password=password
            )

            if user is not None:
                login(request,user)
                return redirect("deshboard")
            else:
                context={
                    "error":"Invalid username or Password"
                }
                return render(request,"login.html",context)
    except Exception as e:
        print(e)
    return render(request,"login.html",context)


def deshboard(request):
    sub=Subjects.objects.all()
    sub_count=Subjects.objects.count()
    topic_count=Topics.objects.count()
    practical_count=Subjects.objects.filter(sub_nature="Practical").count()
    theory_count=Subjects.objects.filter(sub_nature="Theory").count()
    sum=0
    for i in sub:
        sum=sum+i.prog
    average=int(sum/sub_count)
        
    context={
        "data":sub,
        "sub_count":sub_count,
        "topic_count":topic_count,
        "practical_count":practical_count,
        "theory_count":theory_count,
        "progress":average
    }
    return render(request,"deshboard.html",context)