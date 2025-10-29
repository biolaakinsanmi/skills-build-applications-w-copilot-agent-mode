"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet
from django.http import JsonResponse
import os

def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', '')
    base_url = f"https://{codespace_name}-8000.app.github.dev" if codespace_name else "http://localhost:8000"
    return JsonResponse({
        "activities": f"{base_url}/api/activities/",
        "teams": f"{base_url}/api/teams/",
        "users": f"{base_url}/api/users/",
        "leaderboard": f"{base_url}/api/leaderboard/",
        "workouts": f"{base_url}/api/workouts/",
    })

router = routers.DefaultRouter()
import os
codespace_name = os.environ.get('CODESPACE_NAME')
base_url = f'https://{codespace_name}-8000.app.github.dev' if codespace_name else 'http://localhost:8000'
# Example full API endpoint URLs:
# Activities: f"{base_url}/api/activities/"
# Users: f"{base_url}/api/users/"
# Teams: f"{base_url}/api/teams/"
# Leaderboard: f"{base_url}/api/leaderboard/"
# Workouts: f"{base_url}/api/workouts/"
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]
