from django.shortcuts import render
from app1.models import student
from app1.forms import studentform
def name(request):
    a=student.objects.all()
    return render(request,'work1.html',{"k":a})
def form1(request):
    form=studentform()
    if request.method== 'POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return name(request)
        else:
            form=studentform()
    return render(request, 'home1.html', {"form":form})        

def form2(request):
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return name(request)
    return render(request, 'form2.html')

def form3(request):
    if request.method=='POST':
        k=request.POST['n']
        p=request.POST['a']
        o=student.objects.create(name=k,age=p)
        o.save()
        return name(request)
    return render(request, 'forms3.html')
