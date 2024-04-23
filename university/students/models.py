from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

"""
A class representing students.

Attributes:
    first_name (str): The first name of the student.
    middle_name (str): The middle name of the student.
    last_name (str): The last name of the student.
    address (str): The address of the student.
    birth_country (str): The birth country of the student.
    email (str): The email address of the student.
    date_of_birth (datetime.date): The date of birth of the student.
    gender (str): The gender of the student.
    cellphone (str): The phone number of the student.

Methods:
    __str__(): Returns a string representation of the student.
"""


class Students(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        OTHER = "X", "Other"

    first_name = models.CharField(
        max_length=50, verbose_name="First Name", help_text="Enter your first name"
    )
    middle_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Middle Name",
        help_text="Enter your middle name",
    )
    last_name = models.CharField(
        max_length=50, verbose_name="Last Name", help_text="Enter your last name"
    )
    address = models.TextField(
        max_length=254, verbose_name="Address", help_text="Enter your address"
    )
    birth_country = CountryField(
        null=False, blank=False, help_text="Select your birth country"
    )
    email = models.EmailField(
        null=False, verbose_name="Email Address", help_text="Enter your email"
    )
    date_of_birth = models.DateField(help_text="Enter your birthdate")
    gender = models.CharField(
        max_length=1,
        null=False,
        blank=False,
        choices=GenderChoices.choices,
        help_text="Select your gender",
    )
    cellphone = PhoneNumberField(
        unique=True, help_text="Enter your phone number")

    class Meta:
        db_table = "students"

    def __str__(self) -> str:
        return "({0}) {1}, {2}".format(self.id, self.last_name, self.first_name)
