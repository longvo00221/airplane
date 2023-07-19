from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flights(models.Model):
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination} in {self.duration} minutes."
    def is_valid_flight(self):
        return self.origin != self.destination or self.duration > 0


class Passenger(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=25)
    flights = models.ManyToManyField(
        Flights, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
