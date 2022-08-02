from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from alunos.api import viewsets as alunosviewSet

route = routers.DefaultRouter()

route.register(r'alunos', alunosviewSet.AlunosViewSet, basename="Alunos")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(route.urls))
]
