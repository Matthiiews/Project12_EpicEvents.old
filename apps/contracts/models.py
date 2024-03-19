from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _


class Contract(models.Model):
    SIGNED = "S"
    DRAFT = "D"

    STATE_CHOICES = {SIGNED: _("Signed"), DRAFT: _("Draft")}

    client = models.ForeignKey("accounts.Client", on_delete=models.CASCADE,
                               related_name="contract_clients",
                               verbose_name=_("Client of contract"))
    employee = models.ForeignKey("accounts.Client", on_delete=models.CASCADE,
                                 related_name="contract_employee",
                                 verbose_name=_("Client of employee"))
    total_costs = models.DecimalField(max_digits=9, decimal_places=2,
                                      verbose_name=_("Total costs of contract"))
    amount_paid = models.DecimalField(max_digits=9, decimal_places=2,
                                      verbose_name=_("Paid amount of contrat"))
    create_date = models.DateTimeField(auto_now_add=True,
                                       verbose_name=_("Contract created on"))
    state = models.CharField(max_length=1, choices=STATE_CHOICES,
                             default=DRAFT, verbose_name=_("State"))

    @property
    def total(self):
        return f"{self.total_costs} €"

    @property
    def paid_amount(self):
        return f"{self.amount_paid} €"

    @property
    def rest_amount(self):
        # Convert the fields to Decimal before performing the calculation
        total_costs_decimal = Decimal(str(self.total_costs))
        amount_paid_decimal = Decimal(str(self.amount_paid))

        rest_amount = total_costs_decimal - amount_paid_decimal

        return f"{rest_amount} €"

    def __str__(self):
        return f"{self.client.get_full_name} ({self.employee.user.email})"
