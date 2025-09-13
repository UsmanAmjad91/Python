from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tutorial
from .serializers import TutorialSerializer

@api_view(['GET', 'POST'])
def tutorial_list(request):
    """
    List all tutorials or create a new one.
    """
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        serializer = TutorialSerializer(tutorials, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TutorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def tutorials_published(request):
    tutorials = Tutorial.objects.filter(published=True)
    serializer = TutorialSerializer(tutorials, many=True)
    return Response(serializer.data)

