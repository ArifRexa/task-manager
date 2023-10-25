from rest_framework import serializers
from .models import Task, TaskImage
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')  # You can include more fields if needed


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Task
        fields = '__all__'

class TaskNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title')

class TaskImageSerializer(serializers.ModelSerializer):
    tasks = TaskNameSerializer()
    class Meta:
        model = TaskImage
        fields = '__all__'



# http://127.0.0.1:8000/tasks/api/tasks/
# http://127.0.0.1:8000/tasks/api/tasks/images/
