from django.contrib import admin
from .models import Player, Task, Reward, RedeemedReward, CompletedTask


class PlayerAdmin(admin.ModelAdmin):
    queryset = Player.objects.all()
    list_display = ('name', 'score', 'created_at', 'updated_at', 'user', 'id',)


class TaskAdmin(admin.ModelAdmin):
    queryset = Task.objects.all()
    list_display = ('name', 'task', 'points', 'created_at', 'updated_at', 'id',)


class RewardAdmin(admin.ModelAdmin):
    queryset = Reward.objects.all()
    list_display = ('name', 'reward', 'cost', 'id',)


class RedeemedRewardAdmin(admin.ModelAdmin):
    queryset = RedeemedReward.objects.all()
    list_display = ('reward', 'player', 'created_at', 'id',)


class CompletedTaskAdmin(admin.ModelAdmin):
    queryset = CompletedTask.objects.all()
    list_display = ('task', 'player', 'created_at', 'id',)


admin.site.register(Player, PlayerAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Reward, RewardAdmin)
admin.site.register(RedeemedReward, RedeemedRewardAdmin)
admin.site.register(CompletedTask, CompletedTaskAdmin)
