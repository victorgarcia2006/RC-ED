from django.urls import path, include
from rest_framework import routers
from .views import ExperimentDataView, SimulationView


router = routers.DefaultRouter()
#router.register(r'experiments', ExperimentViewSet)
router.register(r'experiment-data', ExperimentDataView, basename="experiment-data")
router.register(r'simulation-data', SimulationView, basename="simulation-data")

urlpatterns = [
    path('monitoreo/', include(router.urls)),
]