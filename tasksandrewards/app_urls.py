"""tasks_and_rewards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import (
    PlayerDetailView,
    PlayerListView,
    HomePageView,
    TaskList,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    TaskDetail,
    RewardList,
    RewardDetail,
    RewardCreate,
    RewardUpdate,
    RewardDelete,
)


app_name = 'app'

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),
    path('players/', PlayerListView.as_view(), name='player-list'),
    path('players/<int:pk>', PlayerDetailView.as_view(), name='player-detail'),
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/view/<int:pk>', TaskDetail.as_view(), name='task-detail'),
    path('tasks/new', TaskCreate.as_view(), name='task-create'),
    path('tasks/edit/<int:pk>', TaskUpdate.as_view(), name='task-edit'),
    path('tasks/delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
    path('rewards/', RewardList.as_view(), name='reward-list'),
    path('rewards/view/<int:pk>', RewardDetail.as_view(), name='reward-detail'),
    path('rewards/new', RewardCreate.as_view(), name='reward-create'),
    path('rewards/edit/<int:pk>', RewardUpdate.as_view(), name='reward-edit'),
    path('rewards/delete/<int:pk>', RewardDelete.as_view(), name='reward-delete'),


]
