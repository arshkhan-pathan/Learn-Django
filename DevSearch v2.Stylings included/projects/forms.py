from django.forms import ModelForm
from .models import Project
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title","description","demo_link",'featured_image',"source_link","tags"]

        widgets={

            "tags":forms.CheckboxSelectMultiple()
        } 
    
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})    
        # setting classs attribs here wow!!!!
        for name,fields in self.fields.items():
            fields.widget.attrs.update({"class":"input"})