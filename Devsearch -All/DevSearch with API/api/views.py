
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project,Review
from api import serializers

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRoutes(request):
     
    routes=[

        {'GET':'api/projects'},
        {'GET':'api/projects/id'},
        {'POST':'api/projects/id/vote'},

        {'POST':'api/users/token'},
        {'POST':'api/users/token/refresh'},

    ]
    
    return Response(routes)

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def getProjects(requests):
    projects=Project.objects.all()
    serializer= ProjectSerializer(projects,many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getProject(requests,pk):
    project=Project.objects.get(id=pk)
    serializer= ProjectSerializer(project,many=False)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def projectVote(request,pk):
    project=Project.objects.get(id=pk)
    user=request.user.profile  #will get user profile from JWT
    data=request.data          #will fetch body data

    review,created=Review.objects.get_or_create(
        owner=user,
        project=project

    )     #Django get_or_create returns the object that it got and a boolean value that specifies whether the object was created or not. 

    review.value=data["value"]
    review.save()
    project.getVoteCount   #will update vote count

    serializer=ProjectSerializer(project,many=False)
    return Response(serializer.data)