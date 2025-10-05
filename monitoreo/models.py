from django.db import models

class Experiment(models.Model):
    name = models.CharField(max_length=100)
    R = models.FloatField(help_text="Resistencia en Ohmios")
    C = models.FloatField(help_text="Capacitancia en Faradios")
    V0 = models.FloatField(help_text="Voltaje inicial")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.created.strftime('%Y-%m-%d %H:%M')})"


class ExperimentData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    voltage = models.FloatField(help_text="Voltaje medido en V")

    def __str__(self):
        return f"Exp {self.timestamp} - {self.voltage:.2f} V"


class SimulationData(models.Model):
    timestamp = models.FloatField(help_text="Tiempo de simulación en segundos")
    voltage = models.FloatField(help_text="Voltaje calculado con Euler")
    h = models.FloatField(help_text="Paso usado en Euler (s)")

    def __str__(self):
        return f"Sim t={self.timestamp:.3f} s - v={self.voltage:.2f} V"

