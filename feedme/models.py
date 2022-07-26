"""
Model created to represent a booking form.
Individual fields are booking components.
Contents in field parentheses represent booking restrictions.
"""
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User


class Booking(models.Model):
    """
    Class to represent booking model
    in database and for booking form.
    """
    user = models.ForeignKey(User,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    customer = models.CharField(max_length=20, null=True)
    phone_number = models.CharField(null=True, blank=True, max_length=20)
    booking_date = models.DateTimeField(null=True)
    booking_time = models.TimeField(null=True)
    people = models.PositiveIntegerField(
                            null=True,
                            validators=[MinValueValidator(1)])
    created_on = models.DateTimeField(auto_now_add=True)

    def validate_date(booking_date):
        """
        Function to validate date so that
        booking date is not in the past.
        """
        if booking_date < timezone.now():
            raise ValidationError("Date cannot be in the past")
    booking_date = models.DateTimeField(
                                null=True,
                                blank=True,
                                validators=[validate_date])

    class Meta:
        """
        Class container with metadata
        attached to the model.
        """
        unique_together = ['user', 'booking_date', 'booking_time']
        ordering = ["created_on"]

    def __str__(self):
        """
        Function to return object model
        items as string.
        """
        return f'{self.customer} has made a booking for {self.people} \
         customers for {self.booking_date}.'
