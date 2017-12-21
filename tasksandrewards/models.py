from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=None)


class Task(models.Model):
    name = models.CharField(max_length=250)
    task = models.TextField(max_length=1000)
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reward(models.Model):
    name = models.CharField(max_length=250)
    reward = models.TextField(max_length=1000)
    cost = models.IntegerField()


class RedeemedReward(models.Model):
    reward = models.ForeignKey('Reward', on_delete=models.CASCADE)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def points_cost(self):
        return self.reward.cost

    def change_player_score(self):
        current_score = self.player.score
        if current_score >= self.points_cost():
            adjusted_score = current_score - self.points_cost()
            self.player.score = adjusted_score
            return self.player.save(update_fields=['score'])
        else:
            print(
                "not enough points to redeem. You need {} points, but you only have {} points".format(self.points_cost,
                                                                                                      current_score))


class CompletedTask(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def points_earned(self):
        return self.task.points

    def change_player_score(self):
        current_score = self.player.score
        adjusted_score = self.points_earned() + current_score
        self.player.score = adjusted_score
        return self.player.save(update_fields=['score'])

