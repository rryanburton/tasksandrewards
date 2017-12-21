from django.conf.urls import url, include
from rest_framework import routers
from tasksandrewards import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'rewards', views.RewardViewSet)
router.register(r'redeemedrewards', views.RedeemedRewardViewSet)
router.register(r'completedtasks', views.CompletedTaskViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]