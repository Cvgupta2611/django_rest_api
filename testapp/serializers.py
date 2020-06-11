from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class Student_serializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Student
        fields = ('id','name','roll_no','collage','owner')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']