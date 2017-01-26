from django.shortcuts import render, redirect

from .models import Catalog

def index(request):
    #Catalog.objects.create(course_name="new courses", description="new courses are always being added!")
    catalog = Catalog.objects.all()
    context = {
        "courses": catalog
    }
    print (catalog)
    return render(request, "firstapp/index.html", context)
    
def add(request):
    if request.method == "POST":
        new_course = request.POST['new_course']
        new_desc = request.POST['new_desc']
        print "new course is ", new_course
        print "description for above is: ", new_desc
        Catalog.objects.create(course_name=new_course, description=new_desc)

    return redirect('/')

#def delete(request, id):
#    print "course id to be deleted is ", id
#    Catalog.objects.filter(id=id).delete()
#    return redirect('/')

#   original delete function above.

def delete(request, id):
    course = Catalog.objects.filter(id=id)
    context = {
        "dcourse": course
    }
    return render(request, "firstapp/delete.html", context)

def confirmed(request, id):
    Catalog.objects.filter(id=id).delete()
    return redirect('/')
