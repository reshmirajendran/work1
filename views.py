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



