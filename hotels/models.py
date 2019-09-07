from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
	name = models.CharField(max_length=150)
	location = models.CharField(max_length=150)
	price_per_night = models.DecimalField(max_digits=10, decimal_places=3)

	def __str__(self):
		return self.name


class Booking(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="bookings")
	check_in = models.DateField()
	number_of_nights = models.PositiveIntegerField()

	def __str__(self):
		return "%s in %s" % (str(self.user), self.hotel.name)
