from django.db import models
import uuid
from users.models import Profile

# Create your models here.
# All database Models will be defined Here

class Project(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    title=models.CharField(max_length=2000)
    description=models.TextField(null=True,blank=True)
    featured_image=models.ImageField(null=True,blank=True,default="default.jpg")
    demo_link=models.CharField(max_length=2000,null=True,blank=True)
    source_link=models.CharField(null=True,blank=True,max_length=2000)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    tags=models.ManyToManyField("Tag",blank=True)              #many to many fields
    vote_total=models.IntegerField(default=0,null=True,blank=True)
    vote_ratio=models.IntegerField(default=0,null=True,blank=True)

    # For Naming our Class better
    def __str__(self):
        return self.title      
    
class Review(models.Model):
    VOTE_TYPE=(('up','UpVote'),('down','DownVote'))   
    project=models.ForeignKey(Project,on_delete=models.CASCADE)  #cascade will delete the entire   /// Foreinn Key REF
    body=models.TextField(null=True,blank=True)
    value=models.CharField(max_length=200,choices=VOTE_TYPE)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self) -> str:
        return self.value
    
class Tag(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self) -> str:
        return self.name
    



