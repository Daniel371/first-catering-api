from django.db import models


class Profile(models.Model):
    card_id = models.CharField(max_length=16, unique=True)
    employee_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=13)
    pin = models.CharField(max_length=4)
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.employee_id}"

    class Meta:
        verbose_name_plural = "User Profiles"
