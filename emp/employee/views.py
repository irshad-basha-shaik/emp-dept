from django.shortcuts import render
from . models import School,Department
# Create your views here.

def home(request):
    res = School.objects.all()
    res1 = Department.objects.all()
    return render(request,"home.html",{"form_list":res,"depts":res1})
def saveform(request):
    res = School.objects.all()
    if request.method=="POST":
        form = School(email=request.POST['email'], depid=request.POST['depid'], name=request.POST['name'], contact=request.POST['contact'])
        form.save()

    return render(request, "loe.html", {"form_list": res})


def edit(request):
    id = request.GET['id']
    d = School.objects.get(id=id)
    d1 = Department.objects.all()
    return render(request,"edit.html",{"form":d,"depts":d1})

def editform(request):
    res = School.objects.all()
    d = School.objects.filter(id=request.POST['id']).update(email=request.POST['email'],name=request.POST['name'], contact=request.POST['contact'],depid=request.POST['departments'])
    return render(request,"loe.html",{"form_list": res})
def delete(request):
    res = School.objects.all()
    d = School.objects.filter(id=request.GET['id']).delete()
    return render(request, "loe.html",{"form_list":res})

def dentry(request):
    if request.method == 'POST':
        d=Department(dname=request.POST['dname'])
        d.save()
        return dmenu(request)
    return render(request,"dentry.html",{})

def dmenu(request):
    res=Department.objects.all()
    return render(request,"dmenu.html",{"form_list":res})