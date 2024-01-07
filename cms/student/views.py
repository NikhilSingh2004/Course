from .models import Student
from .forms import StudentCreation
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Function to display the Home Page
def Home(request : HttpRequest) -> HttpResponse:
    students = Student.objects.all()
    return render(request, 'student/home.html', {
        'students' : students
    })

# Function to display the About Page
def About(request : HttpRequest) -> HttpResponse:
    return render(request, 'student/about.html')

# Function to display the Contact Page
def Contact(request : HttpRequest) -> HttpResponse:
    return render(request, 'student/contact.html')

# Function to Add an Student record
def AddStudent(request: HttpRequest) -> HttpResponse:
    student_create = StudentCreation()
    if request.method == "POST":
        try:
            frm = StudentCreation(data=request.POST)
            if frm.is_valid():
                name = frm.cleaned_data['student_name']
                email = frm.cleaned_data['student_email']
                contact = frm.cleaned_data['student_contact']

                student = Student.objects.create(s_name=name, s_email=email, s_contact=contact)
                student.save()
                return HttpResponseRedirect('/')
            
            return render(request, 'student/addStudent.html', {'form', student_create})
        except Exception as e:
            print(e.__str__())
            return render(request, 'student/addStudent.html', {'form' : student_create})
    else:
        return render(request, 'student/addStudent.html', {'form' : student_create})

# Function to Edit an Student record
def EditStudent(request, id) -> HttpResponse:
    student_object = Student.objects.filter(id=id)[0]
    form = StudentCreation(instance=student_object)
    if student_object:
        if request.method == "POST":
            try:
                form = StudentCreation(request.POST)

                if form.is_valid():
                    student_object.s_name = form.cleaned_data['student_name']
                    student_object.s_email = form.cleaned_data['student_email']
                    student_object.s_contact = form.cleaned_data['student_contact']

                    student_object.save()

                    return HttpResponseRedirect('/')

                return render(request, 'student/editStudent.html', {'form' : form, 'id' :id})
            except Exception as e:
                print(e.__str__())
                return render(request, 'student/editStudent.html', {'form' : form, 'id' :id})
        else:
            return render(request, 'student/editStudent.html', {'form' : form, 'id' :id})
    else:
        return HttpResponseRedirect('/')
    
# Function to Delete an Student record
def DeleteStudent(request, id) -> HttpResponse:
    student_object = Student.objects.filter(id=id)[0]
    if student_object:
        student_object.delete()
        print('Success')
        return HttpResponseRedirect('/')            
    else:
        print('Fail')
        return HttpResponseRedirect('/')