from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from rest_framework import viewsets
from django.contrib.auth.models import Group
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, \
    DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from tasksandrewards.serializers import (
        UserSerializer,
        GroupSerializer,
        PlayerSerializer,
        TaskSerializer,
        RewardSerializer,
        RedeemedRewardSerializer,
        CompletedTaskSerializer
    )
from tasksandrewards.models import User, Coach, Player, Task, Reward, RedeemedReward, CompletedTask, Team

from tasksandrewards.forms import CompletedTaskForm, RedeemRewardForm
# #######  API Views  #######################################


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


# #######  APP Views  #######################################

class HomePageView(TemplateView):
    template_name = 'tasksandrewards/home.html'


class PlayerListView(LoginRequiredMixin, ListView):
    model = Player

    def get_queryset(self):
        coach = Coach.objects.get(user=self.request.user)
        players = Player.objects.filter(team__coaches__name__exact=coach)
        print("coach= {}, players= {}".format(coach, players))
        return players

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coach = Coach.objects.get(user=self.request.user)
        context['coach'] = coach
        team = coach.team
        context['team'] = team
        # context['now'] = timezone.now()
        return context


class PlayerDetailView(LoginRequiredMixin, DetailView):
    model = Player

    tasks = Task.objects.all()
    rewards = Reward.objects.all()
    # completed_tasks = CompletedTask.objects.all().order_by('-created_at')
    # ct in player.completedtask_set.all
    form = CompletedTaskForm(
        initial={
            'task': "task"
        }
    )

    # if form.is_valid():
    #     form.save()
     # context['form'] = self.form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.tasks
        context['rewards'] = self.rewards
        context['form'] = self.form
        # context['completed_tasks'] = self.completed_tasks
        return context


class TaskList(ListView):
    model = Task


class TaskDetail(DetailView):
    model = Task


class TaskCreate(CreateView):
    model = Task
    fields = ('name', 'task', 'points')
    success_url = reverse_lazy('app:task-list')


class TaskUpdate(UpdateView):
    model = Task
    fields = ('name', 'task', 'points')
    success_url = reverse_lazy('app:task-list')


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('app:task-list')


class RewardList(ListView):
    model = Reward


class RewardDetail(DetailView):
    model = Reward


class RewardCreate(CreateView):
    model = Reward
    fields = ('name', 'reward', 'cost')
    success_url = reverse_lazy('app:reward-list')


class RewardUpdate(UpdateView):
    model = Reward
    fields = ('name', 'reward', 'cost')
    success_url = reverse_lazy('app:reward-list')


class RewardDelete(DeleteView):
    model = Reward
    success_url = reverse_lazy('app:reward-list')


class CompletedTaskCreate(CreateView):
    model = CompletedTask
    fields = ('task', 'player')

    def get_success_url(self):
        formkwargs = self.get_form_kwargs()
        playerid=formkwargs['data']['player']
        return reverse_lazy('app:player-detail', kwargs={'pk': playerid})


# @register.filter(name='subtract')
# def subtract(value, arg):
#     return value - arg

class CompleteTaskInTemplate(CompletedTaskCreate):
    template_name = "tasksandrewards/completedtask_form.html"

    def complete_task(request):
        if request.method == 'POST':
            print("it's post")
            form = CompletedTaskForm(request.POST)
            print(form)

class RedeemedRewardCreate(CreateView):
    model = RedeemedReward
    fields = ('reward', 'player')

    def get_success_url(self):
        formkwargs = self.get_form_kwargs()
        playerid=formkwargs['data']['player']
        return reverse_lazy('app:player-detail', kwargs={'pk':playerid})

class RedeemRewardInTemplate(RedeemedRewardCreate):
    template_name = "tasksandrewards/redeemedreward_form.html"

    def redeem_reward(request):
        if request.method == 'POST':
            print("it's post")
            form = RedeemRewardForm(request.POST)
            print(form)


# def CompletedTaskinTemplate(
#         self,
#         # request,
#         task,
#         player
# ):
#
#
#     task = Task.objects.get(pk=task)
#     player = Player.objects.get(pk=player)
#     print("task: {}".format(task))
#     newtask = CompletedTask.objects.create(task=task, player=player)
#     newtask.full_clean()
#     newtask.save()
#     print("newtask: {}".format(newtask))
#     playerid = player.id
#     print("player {} id: {}".format(player.name, playerid))
#     # return render(request, 'tasksandrewards/player_detail.html', kwargs={'pk': playerid})
#     return reverse('app:player-detail', kwargs={'pk': playerid})
