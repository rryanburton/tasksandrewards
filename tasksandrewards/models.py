from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50)


class Score(models.Model):
    score = models.IntegerField()
    player = models.ForeignKey('Player', on_delete=models.CASCADE,)


class Task(models.Model):
    name = models.CharField(max_length=250)
    task = models.TextField(max_length=1000)
    points = models.IntegerField()


class Reward(models.Model):
    name = models.CharField(max_length=250)
    reward = models.TextField(max_length=1000)
    cost = models.IntegerField()





