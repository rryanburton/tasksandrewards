from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Player, Coach, Team, Task, Reward, RedeemedReward, CompletedTask


class PlayerAdmin(admin.ModelAdmin):
    queryset = Player.objects.all()
    list_display = (
        'name',
        'team',
        'score',
        'created_at', 'updated_at', 'user', 'id',)


class CoachAdmin(admin.ModelAdmin):
    queryset = Coach.objects.all()
    list_display = (
        'name',
        'team',
        'created_at', 'updated_at', 'user', 'id',)


# class PlayerInline(admin.TabularInline):
#     model = Player
#     fields = ('name',)


class TeamAdmin(admin.ModelAdmin):
    queryset = Team.objects.all()
    # inlines = [PlayerInline]

    def players_display(self, obj):
        return ", ".join([
            member.name for member in obj.players.all()
        ])
    players_display.short_description = 'players'

    def coaches_display(self, obj):
        return ", ".join([
            member.name for member in obj.coaches.all()
        ])
    coaches_display.short_description = 'coaches'
    list_display = ('name', 'created_at', 'updated_at', 'id', 'players_display', 'coaches_display')




class TaskAdmin(admin.ModelAdmin):
    queryset = Task.objects.all()
    list_display = ('name', 'task', 'points', 'created_at', 'updated_at', 'id',)


class RewardAdmin(admin.ModelAdmin):
    queryset = Reward.objects.all()
    list_display = ('name', 'reward', 'cost', 'id',)


class RedeemedRewardAdmin(admin.ModelAdmin):
    queryset = RedeemedReward.objects.all()
    list_display = ('reward', 'points_cost', 'player', 'created_at', 'id',)


class CompletedTaskAdmin(admin.ModelAdmin):
    queryset = CompletedTask.objects.all()
    list_display = ('task', 'points_earned', 'player', 'created_at', 'id',)


admin.site.register(User, UserAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Reward, RewardAdmin)
admin.site.register(RedeemedReward, RedeemedRewardAdmin)
admin.site.register(CompletedTask, CompletedTaskAdmin)
