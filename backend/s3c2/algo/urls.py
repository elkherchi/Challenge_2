from django.urls import path
from . import views

urlpatterns = [
    path('calculate-distances/', views.calculate_distances, name='calculate_distances'),
    path('tsp-solution/', views.tsp_solution, name='tsp_solution'),
    path('ant-system-solution/', views.ant_system_solution, name='ant_system_solution'),
]
