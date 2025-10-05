from rest_framework import serializers
from .models import Experiment, ExperimentData, SimulationData

class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = "__all__"

class ExperimentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentData
        fields = "__all__"

class SimulationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimulationData
        fields = "__all__"
