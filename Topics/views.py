from django.shortcuts import render,redirect
from .models import Topics
from Subjects.models import Subjects

# Create your views here.
def alltopics(request):
    sub=Subjects.objects.all()
    data=Topics.objects.all()
    context={
        "sub":sub,
        "data":data
    }
    return render(request,"topics/alltopics.html",context)


def add(request):
    data=Subjects.objects.all()
    t_data=Topics.objects.all()
    try:
        if(request.method=="POST"):
            topic_id=request.POST.get("topic_id")
            sub_id=request.POST.get("sub_id")
            topic_name=request.POST.get("topic_name")
            topic_nature=request.POST.get("topic_nature")
            date_studied=request.POST.get("date_studied")
            difficulty=request.POST.get("difficulty")
            self_study=request.POST.get("self_study")
            overview=request.POST.get("overview")

            for i in t_data:
                if(sub_id == i.sub_id_id and topic_name==i.topic_name):
                    context={
                        "error":"This Topic is already exsists in same subject"
                    }
                    return render(request,"topics/add.html",context)
                # print(i.sub_id_id,end="")
                # print(sub_id)
                # print(i.topic_name,end="")
                # print(topic_name)
            
            
                
            Topics.objects.create(
                topic_id=topic_id,
                sub_id_id=sub_id,
                topic_name=topic_name,
                topic_nature=topic_nature,
                date_studied=date_studied,
                difficulty=difficulty,
                self_study=self_study,
                overview=overview
            )
            

            print("added")
            return redirect("alltopics")
    except Exception as e:
        print("error:",e)
    context={
        "sub":data
    }
    return render(request,"topics/add.html",context)


def update(request,topic_id):
    try:
        data=Topics.objects.get(topic_id=topic_id)
        sub=Subjects.objects.all()
        if(request.method=="POST"):
            topic_id=request.POST.get("topic_id")
            sub_id=request.POST.get("sub_id")
            topic_name=request.POST.get("topic_name")
            topic_nature=request.POST.get("topic_nature")
            date_studied=request.POST.get("date_studied")
            difficulty=request.POST.get("difficulty")
            self_study=request.POST.get("self_study")
            overview=request.POST.get("overview")

            data.topic_id=topic_id
            data.sub_id_id=sub_id
            data.topic_name=topic_name
            data.topic_nature=topic_nature
            data.date_studied=date_studied
            data.difficulty=difficulty
            data.self_study=self_study
            data.overview=overview
            data.save()
            print("updated")
            return redirect("alltopics")
    except Topics.DoesNotExist:
            context={
                "error":"Not Found Topic with this name"
            }
            return render(request,"topics/update.html",context)
    context={
        "data":data,
        "sub":sub
    }
    return render(request,"topics/update.html",context)

def delete(request,topic_id):
    data=Topics.objects.get(topic_id=topic_id)
    data.delete()
    return redirect("alltopics")

def searchupdate(request):
    try:
        if(request.method=="POST"):
            s=request.POST.get("s")
            return redirect("update",topic_id=s)
    except:
        pass
    return render(request,"topics/update.html")

def searchdelete(request):
    try:
        if(request.method=="POST"):
            s=request.POST.get("s")
            return redirect("delete",topic_id=s)
    except:
        pass
    return render(request,"topics/delete.html")

def delete(request,topic_id):
    try:
        data=Topics.objects.get(topic_id=topic_id)
        context={
            "data":data
        }
    except Topics.DoesNotExist:
        context={
            "error":"Not found Topic with this Name"
        }
    return render(request,"topics/delete.html",context)

def confirm(request,topic_id):
    a_data=Topics.objects.get(topic_id=topic_id)
    try:
        if(request.method=="POST"):
            c=request.POST.get("c")
            if(c=="Yes"):
                return redirect("maindelete",topic_id=topic_id)
            else:
                return redirect("alltopics")
    except:
        pass
    context={
        "a_data":a_data,
        "con":"yes"
    }
    return render(request,"topics/delete.html",context)

def maindelete(request,topic_id):
    data=Topics.objects.get(topic_id=topic_id)
    data.delete()
    return redirect("alltopics")

def searchtopic(request):
    try:
        if(request.method=="POST"):
            s=request.POST.get("s")
            return redirect("singletopic",topic_name=s)
    except:
        pass
    return render(request,"topics/singletopic.html")


def singletopic(request,topic_name):
    try:
        data=Topics.objects.filter(topic_name=topic_name)
        context={
            "data":data
        }
    except Topics.DoesNotExist:
        context={
            "error":"Not found Topic with this Name"
        }
    return render(request,"topics/singletopic.html",context)


