from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    contract = models.ForeignKey(
        "contracts.Contract", on_delete=models.CASCADE,
        related_name="Event_contracts", verbose_name=_("Contract for event"))

    employee = models.ForeignKey(
        "accounts.Employee", on_delete=models.CASCADE,
        related_name="event_employees",
        verbose_name=_("employee for event"))

    date = models.DateTimeField(
        default=timezone.now, verbose_name=_("Date of event"))

    name = models.CharField(
        max_length=100, verbose_name=_("Name of event"))

    location = models.CharField(
        max_length=200, verbose_name=_("Address of event"))

    max_guests = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(
            1,
            _("Impossible to create an event with the number of guest less than 1 guest."))],
        verbose_name=_("Number of guests"))
    notes = models.TextField(verbose_name=_("notes for the event"))

    def __str__(self):
        return f"{self.name} ({self.employee.user.email})"


# Create your models here.
