from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Player(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=None)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=250)
    task = models.TextField(max_length=1000)
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.name , self.points)


class Reward(models.Model):
    name = models.CharField(max_length=250)
    reward = models.TextField(max_length=1000)
    cost = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.name , self.cost)


class RedeemedReward(models.Model):
    reward = models.ForeignKey('Reward', on_delete=models.CASCADE)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def points_cost(self):
        return self.reward.cost

    def change_player_score(self):
        current_score = self.player.score
        if current_score >= self.reward.cost:
            adjusted_score = current_score - self.reward.cost
            self.player.score = adjusted_score
            print("changing player score")
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
        # print("instance: {}".format(self))
        current_score = self.player.score
        adjusted_score = self.task.points + current_score
        self.player.score = adjusted_score
        # print(" task changing player score")
        return self.player.save(update_fields=['score'])


def model_created_or_updated(sender, **kwargs):
    # print("kwargs: {}".format(kwargs))
    the_instance = kwargs['instance']
    sender.change_player_score(the_instance)


post_save.connect(model_created_or_updated, sender=CompletedTask)
post_save.connect(model_created_or_updated, sender=RedeemedReward)
