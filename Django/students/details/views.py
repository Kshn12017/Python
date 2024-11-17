from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.
def index(request):

    if request.POST:
        name = request.POST['fname']
        lname = request.POST['lname']
        roll = request.POST['roll']

        print(name, lname, roll)

        student = StudentDetail.objects.create(first_name=name, last_name=lname, roll_number=roll)

        student.save()

    stud_all = StudentDetail.objects.all()

    return render(request, 'index.html', {'student': stud_all})


def edit(request, id):

    print(id)
    
    student = get_object_or_404(StudentDetail, id=id)
    
    # student = StudentDetail.object.get(id=id)
    
    if request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        roll = request.POST['roll']

        print(fname, lname, roll)
        
        student.first_name = fname
        student.last_name = lname
        student.roll_number = roll

        student.save()
        
        return redirect(index)
    

    return render(request, 'edit.html', {'student': student})


def delete(request, id):

    print(id)
    
    student = get_object_or_404(StudentDetail, id=id)
    
    if request.POST:
        student.delete()    
        
        return redirect(index)
    
    return render(request, 'delete.html')
