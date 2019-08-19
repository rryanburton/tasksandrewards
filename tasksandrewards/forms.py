from django.forms import ModelForm
from .models import CompletedTask, RedeemedReward


class CompletedTaskForm(ModelForm):
    class Meta:
        model = CompletedTask
        fields = ['task', 'player']


class RedeemRewardForm(ModelForm):
    class Meta:
        model = RedeemedReward
        fields = ['reward', 'player']