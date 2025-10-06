# views.py
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
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
        data = request.data  # Espera una lista de objetos [{t, v}, ...]

        # Validación simple
        if not isinstance(data, list):
            return Response({"error": "El cuerpo de la solicitud debe ser una lista de objetos."}, status=status.HTTP_400_BAD_REQUEST)

        registros = []
        for item in data:
            try:
                tiempo_ms = item.get("t")
                voltaje = item.get("v")
                if voltaje is None or tiempo_ms is None:
                    continue

                registro = ExperimentData(
                    timestamp=tiempo_ms,  # Puedes ajustar si quieres usar tiempo_ms
                    voltage=voltaje
                )
                registros.append(registro)
            except Exception as e:
                print("Error procesando item:", e)

        # Guardado masivo
        ExperimentData.objects.bulk_create(registros)

        return Response({
            "status": "ok",
            "registros_creados": len(registros)
        }, status=status.HTTP_201_CREATED)

    def list(self, request):
        data = ExperimentData.objects.all().order_by("timestamp")
        return Response([{"t": d.timestamp, "v": d.voltage} for d in data])

class SimulationView(viewsets.ModelViewSet):
    def list(self, request):
        #h = float(request.GET.get("h", ro/20))
        #tmax = float(request.GET.get("tmax", 1.0))
        h = ro/10
        n = 80
        t=np.zeros(n+1)
        v=np.zeros(n+1)
        t[0]=0
        v[0]=V0
        for i in range(n):
            v[i+1]=v[i]+h*f(t[i],v[i])
            t[i+1]=t[i]+h
        return Response([{"t": round(t[i], 4), "v": v[i]} for i in range(n)])
