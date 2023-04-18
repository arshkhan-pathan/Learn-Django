# https://www.django-rest-framework.org/api-guide/generic-views/#mixins




from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Task
from .serializers import TaskSerializer
from rest_framework import generics,mixins
from django.shortcuts import get_object_or_404




class TaskMixinView(mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset=Task.objects.all()
    serializer_class=TaskSerializer  
    lookup_field="pk"

    def get(self,request,*args,**kwargs):
        pk=kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        
        return self.list(request,*args,**kwargs)
            
    # def post(self,request,*args,**kwargs):
    #     return self.create(self,request,*args,**kwargs)
    

    #can also perform update and delete refer documentation

       



@api_view(["GET"])
def getTasks(requests):
    Tasks=Task.objects.all()
    serializer= TaskSerializer(Tasks,many=True)
    return Response(serializer.data)


#genereic api
#to get objects by differnrt id override lookup_id
class TaskDetailAPIVIEW(generics.RetrieveAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer    

# To create a class
class TaskCreateAPIVIEW(generics.CreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer      

    #def perform_create()  if want to do some customization while creating foe eg setting default user

class TaskProductListAPIVIEW(generics.ListAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer 

#combining list and create api
# /listcreate/
# can perform both get and post

class TaskCreateListAPIVIEW(generics.ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer  



class TaskUpdateAPIVIEW(generics.UpdateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer  
    def perform_update(self, serializer):
        instance=serializer.save()
        if not instance.description:
            instance.description=instance.title
        # return super().perform_update(serializer)

class TaskDeleteAPIVIEW(generics.DestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    lookup_field="pk"  
    def perform_destroy(self, instance):
        #instance
        super().perform_destroy(instance)        



# Function Based Views


@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):
    method=request.method

    if method=='GET':
        if pk is not None:
            #detail View
            # refers urls .py thiss nested view will have separate route
            obj=get_object_or_404(Task,pk=pk)
            data=TaskSerializer(obj,many=False).data
            return Response(data)
        
        queryset=Task.objects.all()
        data=TaskSerializer(queryset,many=True).data
        return Response(data)
    
    if method=="POST":
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get('title')
            '''
            
            The below lines of code will check if the value of descirptionisgiven or not
            if not then it will set its value to ofthe title
            
            '''
            
            description=serializer.validated_data.get("description") or None
            if description is None:
                description=title
            serializer.save(description=description)
            return Response(serializer.data)
        return Response({"invalid":'Not good data'},status=400)    
    


    

