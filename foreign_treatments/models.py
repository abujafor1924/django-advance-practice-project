from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    flag = models.ImageField(upload_to='flags/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

class Hospital(models.Model):
    country = models.ForeignKey(Country, related_name='hospitals', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='hospital_icons/')
    speciality = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class HospitalDetail(models.Model):
    hospital = models.OneToOneField(Hospital, related_name='details', on_delete=models.CASCADE)
    banner = models.ImageField(upload_to='hospital_banners/')
    description = models.TextField()
    contact_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Details for {self.hospital.name}"





# --------------------------------- bangladesh hospitals ---------------------------------


class Division(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = " Bangladesh Division"
        verbose_name_plural = " Bangladesh Divisions"

    def __str__(self):
        return self.name


class District(models.Model):
    division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE,
        related_name="districts",
    )
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]
        unique_together = ("division", "name")
        verbose_name = "Bangladesh District"
        verbose_name_plural = "Bangladesh Districts"

    def __str__(self):
        return f"{self.name} ({self.division.name})"


class BangladeshHospital(models.Model):
    guardian_id = models.PositiveIntegerField(
        unique=True,
        help_text="Hospital ID from Guardian Life list."
    )

    name = models.CharField(max_length=255)
    
    image = models.ImageField(upload_to='bangladesh_hospital_images/', blank=True, null=True)

    division = models.ForeignKey(
        Division,
        on_delete=models.PROTECT,
        related_name="hospitals",
    )

    district = models.ForeignKey(
        District,
        on_delete=models.PROTECT,
        related_name="hospitals",
    )

    area = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    facilities = models.TextField(blank=True)
    contact_details = models.TextField(blank=True)
    remark = models.TextField(blank=True)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Bangladesh Hospital"
        verbose_name_plural = "Bangladesh Hospitals"
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["division"]),
            models.Index(fields=["district"]),
            models.Index(fields=["area"]),
        ]

    def __str__(self):
        return self.name
    

class InternationalCountry(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "International Country"
        verbose_name_plural = "International Countries"

    def __str__(self):
        return self.name

class InternationalGuardianHospital(models.Model):
    guardian_hospital_id = models.PositiveIntegerField(
        unique=True,
        help_text="Hospital ID from Guardian Life list."
    )

    hospital_name = models.CharField(max_length=255)
    country = models.ForeignKey(
        InternationalCountry,
        on_delete=models.PROTECT,
        related_name="hospitals"
    )
    address = models.TextField()

    discount = models.TextField(blank=True)
    contact_person = models.CharField(max_length=255, blank=True)
    contact_details = models.TextField(blank=True)
    cashless_facility = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "international_guardian_hospitals"
        ordering = ["hospital_name"]

    def __str__(self):
        return self.hospital_name