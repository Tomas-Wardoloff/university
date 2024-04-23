from django.db import models
from django.core.validators import MinValueValidator

"""
A class representing degrees in a database.

Attributes:
    name (str): The name of the degree.
    degree_type (str): The type of the degree.
    total_credits (int): The total number of credits required to obtain the degree.

Methods:
    __str__(): Returns a string representation of the degree.

"""


class Degrees(models.Model):
    class TypeChoices(models.TextChoices):
        ASSOCIATE_DEGREE = "AD", "Associate Degree"
        BACHELOR_DEGREE = "BD", "Bachelor's Degree"
        GRADUATE_DEGREE = "GD", "Graduate Degree"

    name = models.CharField(max_length=50, verbose_name='Degree Name',
                            help_text='Enter the degree name', unique=True)
    degree_type = models.CharField(max_length=2, choices=TypeChoices.choices,
                                   verbose_name='Degree Type', help_text='Select degree type')
    total_credits = models.PositiveIntegerField(
        verbose_name='Total Credits to get', help_text='Insert degree total credits', validators=[MinValueValidator(1)])

    class Meta:
        db_table = "degrees"
        ordering = ['id', 'name', 'degree_type']

    def __str__(self) -> str:
        return "({0}) {1}, type: {2}".format(self.id, self.name, self.degree_type)
