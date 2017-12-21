from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from tasksandrewards.serializers import UserSerializer, GroupSerializer, PlayerSerializer, TaskSerializer, RewardSerializer, RedeemedRewardSerializer, CompletedTaskSerializer
from tasksandrewards.models import Player, Task, Reward, RedeemedReward, CompletedTask

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

class RedeemedRewardViewSet(viewsets.ModelViewSet):
    queryset = RedeemedReward.objects.all()
    serializer_class = RedeemedRewardSerializer

class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = CompletedTask.objects.all()
    serializer_class = CompletedTaskSerializer

