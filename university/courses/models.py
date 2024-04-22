from django.db import models
from degree.models import Degrees

"""
A class representing a course.

Attributes:
    name (str): The name of the course.
    credits (int): The total credits of the course.
    description (str): The description of the course.
    degree_id (Degrees): The foreign key to the Degrees model.
    
Meta:
    ordering (list): The default ordering of the courses based on their names.

Methods:
    __str__(): Returns a string representation of the course.

"""


class Courses(models.Model):
    name = models.CharField(max_length=50, verbose_name='Course Name',
                            help_text='Enter the course name', unique=True)
    credits = models.IntegerField(
        verbose_name='Total Credits', help_text="Enter course's credits")
    description = models.TextField(
        max_length=500, verbose_name='Course Description', help_text='Enter the course description')
    degree_id = models.ForeignKey(Degrees, on_delete=models.PROTECT)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return "Course: ({0}) {1}".format(self.id, self.name)
