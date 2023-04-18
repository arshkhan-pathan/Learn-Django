from rest_framework import serializers
from rest_framework.reverse import reverse
from base.models import Task



class TaskSerializer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField(read_only=True)    # creating model field on go!
    edit_url=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Task
        fields="__all__"
    
    def get_url(self,obj):
        # return f"api/tasks/{obj.pk}"
        request=self.context.get('request')    
        print(request)
        return reverse("product-detail",kwargs={"pk":obj.pk},request=request)    #here idk why but request obj is not working
        if request is None:
            return None
        
    def get_edit_url(self,obj):

        # return f"api/tasks/{obj.pk}"
        request=self.context.get('request')    
        print(request)
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request)       