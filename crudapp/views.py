from django.shortcuts import render, redirect 
from crudapp.models import Student
from crudapp.forms import StudentForm

# Create your views here.




def read_data(request):
    Student_list=Student.objects.all()
    employees = Student.objects.all() 

    return render(request,"home.html",{'student_list':employees})

def readone_data(request,id):#id=5
    student=Student.objects.get(id=id)
    context={
        'student':student
    }
    return render(request,"readone.html",context)

def stud(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  #form.py
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,'index.html',{'form':form})  #index.html

def show(request):  
    employees = Student.objects.all()  
    return render(request,"show.html",{'employees':employees})  

def edit(request, id):  
    employee = Student.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
    
def update(request, id):  
    employee = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  

def destroy(request, id):  
    employee = Student.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  
