from django.contrib.auth.models import  Group
from rest_framework import serializers
from tasksandrewards.models import Coach, User, Player, Task, Reward, RedeemedReward, CompletedTask


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name',)


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups',)


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'score', 'created_at', 'updated_at', 'user', 'id',)


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'task', 'points', 'created_at', 'updated_at', 'id',)


class RewardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reward
        fields = ('name', 'reward', 'cost', 'id',)


class RedeemedRewardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RedeemedReward
        fields = ('reward', 'player', 'created_at', 'id',)


class CompletedTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompletedTask
        fields = ('task', 'player', 'created_at', 'id',)
