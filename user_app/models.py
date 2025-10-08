from django.db import models


# Create your models here.
class Ownersinfo(models.Model):
    name = models.CharField(max_length=100, default="Unknown", blank=True)
    phone = models.CharField(max_length=13, default="Unknown", blank=True)
    division = models.CharField(max_length=50, default="Unknown", blank=True)
    district = models.CharField(max_length=50, default="Unknown", blank=True)
    upazila = models.CharField(max_length=50, default="Unknown", blank=True)
    address = models.CharField(max_length=120, default="Unknown", blank=True)

    def __str__(self):
        return self.phone


class Patientinfo(models.Model):
    # Owner info
    name = models.CharField(max_length=100, default="Unknown")
    phone = models.CharField(max_length=13, default="Unknown")

    # Appointment info
    application_time = models.DateTimeField(auto_now=True)

    # Animal info
    tag = models.CharField(max_length=30, null=True, default="Unknown")
    species = models.CharField(max_length=60, null=True, default="Unknown")
    breed = models.CharField(max_length=50, null=True, default="Unknown")
    weight = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, default=-1
    )
    age = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True, default=-1
    )
    sex = models.CharField(max_length=10, default="female")
    pregnancy = models.BooleanField(default=False)
    pregnancy_month = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True, default=-1
    )
    parity = models.CharField(max_length=10, default="Unknown")
    milk_yield = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True, default=-1
    )
    date_of_parturition = models.DateField(null=True, blank=True)
    date_of_oestrus = models.DateField(null=True, blank=True)

    # Herd info
    total_animals = models.IntegerField(default=-1)
    total_sick_animals = models.IntegerField(default=-1)
    total_dead_animals = models.IntegerField(default=-1)
    duration_of_illness = models.IntegerField(default=-1)

    # Health history
    complaint = models.TextField(default="Unknown", blank=True, null=True)
    disease_history = models.TextField(default="Unknown", blank=True, null=True)
    treatment_history = models.TextField(default="Unknown", blank=True, null=True)
    management_history = models.TextField(default="Unknown", blank=True, null=True)

    def __str__(self):
        return self.phone
