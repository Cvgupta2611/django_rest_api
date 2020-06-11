from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework import status,generics,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from testapp.permissions import IsOwnerOrReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = Student_serializer

@api_view(['GET', 'POST','DELETE'])
def snippet_detail(request,pk=None):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    print('----->>>>',request.data)
    """
    List all code snippets, or create a new snippet.
    """
    try:
        snippet = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = Student_serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def snippet_list(request):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    print('----------<>>>>>>>',request.data,status,'--------------')

    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = Student_serializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Student_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
