from django.shortcuts import render,redirect
from .models import Subjects
from Topics.models import Topics

# Create your views here.
def home(request):
    data=Subjects.objects.all()
    context={
        "data":data
    }
    return render(request,"subjects/home.html",context)

def add(request):
    data=Subjects.objects.all()
    try:
        if(request.method=="POST"):
            print("hello")
            sub_id=request.POST.get("sub_id")
            sub_name=request.POST.get("sub_name")
            sub_code=request.POST.get("sub_code")
            sub_type=request.POST.get("sub_type")
            sub_nature=request.POST.get("sub_nature")
            credit=request.POST.get("credit")
            desc=request.POST.get("desc")
            progress=request.POST.get("progress")
            
            for i in data:
                if(sub_name==i.sub_name):
                    context={
                        "error":"Subject is Already Exists"
                    }
                    return render(request,"subjects/add.html",context)
                
            Subjects.objects.create(
                sub_id=sub_id,
                sub_name=sub_name,
                sub_code=sub_code,
                sub_type=sub_type,
                sub_nature=sub_nature,
                credit=credit,
                desc=desc,
                prog=progress
            )
            print("added")
            return redirect("allsubjects")
    except Exception as e:
        print("error:",e)
    return render(request,"subjects/add.html")


def searchupdate(request):
    try:
        if(request.method=="POST"):
            s=request.POST.get("s")
            return redirect("update",sub_name=s)
    except Exception as e:
        print("error:",e)
    return render(request,"subjects/update.html")

def update(request,sub_name):
    try:
        data=Subjects.objects.get(sub_name=sub_name)
        if(request.method=="POST"):
            sub_id=request.POST.get("sub_id")
            sub_name=request.POST.get("sub_name")
            sub_code=request.POST.get("sub_code")
            sub_type=request.POST.get("sub_type")
            sub_nature=request.POST.get("sub_nature")
            credit=request.POST.get("credit")
            desc=request.POST.get("desc")
            prog=request.POST.get("progress")
    
            data.sub_id=sub_id
            data.sub_name=sub_name
            data.sub_code=sub_code
            data.sub_type=sub_type
            data.sub_nature=sub_nature
            data.credit=credit
            data.desc=desc
            data.prog=prog
            data.save()
            print("Updated")
            return redirect("allsubjects")
        
    except Subjects.DoesNotExist:
        context2={
            "error":"Not found subject with this name"
        }
        return render(request,"subjects/update.html",context2)

    context={
        "data":data
    }
    return render(request,"subjects/update.html",context)


def searchdelete(request):
    try:
        if(request.method=="POST"):
            s=request.POST.get("s")
            return redirect("delete",sub_name=s)
    except:
        pass
    return render(request,"subjects/delete.html")


def delete(request,sub_name):
    topic_count=Topics.objects.count()
    try:
        data=Subjects.objects.get(sub_name=sub_name)
    except Subjects.DoesNotExist:
        context={
            "error":"Not found subject with this name"
        }
        return render(request,"subjects/delete.html",context)
    
    context={
        "topic_count":topic_count,
        "data":data
    }
    return render(request,"subjects/delete.html",context)


def confirm(request,sub_name):
    data=Subjects.objects.get(sub_name=sub_name)
    topic_count=Topics.objects.count()
    try:
        if(request.method=="POST"):
            c=request.POST.get("c")
            if(c=="Yes"):
                return redirect("maindelete",sub_name=sub_name)
            else:
                return redirect("allsubjects")
    except:
        pass
    context={
        "a_data":data,
        "topic_count":topic_count,
        "con":"yes"
    }
    return render(request,"subjects/delete.html",context)


def maindelete(request,sub_name):
    data=Subjects.objects.get(sub_name=sub_name)
    data.delete()
    return redirect("allsubjects")

def searchsinglesub(request):
    try:
        if(request.method=="POST"):
            s=request.POST.get("s")
            return redirect("singlesub",sub_name=s)
    except:
        pass
    return render(request,"subjects/searchsinglesub.html")

def singlesub(request,sub_name):
    topic_count=Topics.objects.count()
    try:
        data=Subjects.objects.get(sub_name=sub_name)
        context={
            "topic_count":topic_count,
            "data":data
        }
    except Exception as e:
        context={
            "error":"Not found Subject with this name"
        }
    return render(request,"subjects/searchsinglesub.html",context)


