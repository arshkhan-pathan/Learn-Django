from django.shortcuts import render,redirect
from .models import  Project
from .forms import ProjectForm


# Create your views here.
# What to show/render on particular page will be defined here
# Along with what data to pass
# A view function, or view for short, is a Python function that takes a web request and returns a web response.  

from django.http import HttpResponse

def projects(request):
    projects=Project.objects.all()
    context={"projects":projects}
    return render(request,template_name="projects/projects.html",context=context)


def project(request,pk):
    # return HttpResponse("Single Project"+" "+str(pk))     #page with dyanamic paramaters/slug
        projectObj=Project.objects.get(id=pk)
        return render(request,"projects/single-project.html",{'project':projectObj})



def createProject(request):

    form=ProjectForm()
    if request.method=="POST":
         print(request.POST)
         form=ProjectForm(request.POST,request.FILES)
         if form.is_valid():
              form.save()
              return redirect("projects")
    
    
    
    context={"form":form}
    return render(request,"projects/project_form.html",context)        


def updateProject(request,pk):    #primary  key to uniquely identify data
    project=Project.objects.get(id=pk)
    form=ProjectForm(instance=project)    #it will prefill form data of selected project
    if request.method=="POST":
         print(request.POST)
         form=ProjectForm(request.POST,request.FILES,instance=project)
         if form.is_valid():
              form.save()
              return redirect("projects")
    
    
    
    context={"form":form}
    return render(request,"projects/project_form.html",context)    


def deleteProject(request,pk):    #primary  key to uniquely identify data
    project=Project.objects.get(id=pk)
    context={"object":project}
    if request.method=="POST":
        project.delete()
        return redirect("projects")
        

        
    
    return render(request,"projects/delete_template.html",context)
    
    
   

        
              

 

