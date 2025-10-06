# views.py
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from .models import ExperimentData
from .serializer import ExperimentSerializer
import math
import numpy as np
# Parámetros RC

V0 = 3.04
R = 5.78e3
C = 100e-6
ro = R*C

def f(t,v):
    return -v/ro

class ExperimentDataView(viewsets.ModelViewSet):
    queryset = ExperimentData.objects.all()
    serializer_class = ExperimentSerializer
    def create(self, request):
        voltage = request.data.get("voltage")
        ts = timezone.now()
        ExperimentData.objects.create(timestamp=ts, voltage=voltage)
        return Response({"status": "ok", "timestamp": ts, "voltage": voltage})

    def list(self, request):
        data = ExperimentData.objects.all().order_by("timestamp")
        return Response([{"t": d.timestamp, "v": d.voltage} for d in data])

class SimulationView(viewsets.ModelViewSet):
    def list(self, request):
        #h = float(request.GET.get("h", ro/20))
        #tmax = float(request.GET.get("tmax", 1.0))
        h = ro/10
        n = 100
        t=np.zeros(n+1)
        v=np.zeros(n+1)
        t[0]=0
        v[0]=V0
        for i in range(n):
            v[i+1]=v[i]+h*f(t[i],v[i])
            t[i+1]=t[i]+h
        return Response([{"t": round(t[i], 4), "v": v[i]} for i in range(n)])
