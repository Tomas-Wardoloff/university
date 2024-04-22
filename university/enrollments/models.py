from django.db import models
from students.models import Students
from courses.models import Courses
from degree.models import Degrees

"""
A class representing the enrollment of a student in a course.

Attributes:
    student_id (ForeignKey): The foreign key to the Students model representing the student enrolled in the course.
    course_id (ForeignKey): The foreign key to the Courses model representing the course in which the student is enrolled.
    enrollment_date (DateField): The date when the student enrolled in the course.
    status (CharField): The status of the student in the course.

    StatusChoices (TextChoices): A nested class defining the choices for the status field.

Meta:
    ordering (list): A list specifying the default ordering of instances in the database.

Methods:
    __str__(): Returns a string representation of the CourseEnrollment instance.

"""


class CourseEnrollment(models.Model):
    class StatusChoices(models.TextChoices):
        ENROLLED = "E", "Enrolled"
        COMPLETED = "C", "Completed"
        PENDING = "P", "Pending"
        FAILED = "F", "Failed"

    student_id = models.ForeignKey(
        Students, verbose_name='Student id', help_text='Select Student Id', on_delete=models.CASCADE)
    course_id = models.ForeignKey(
        Courses, verbose_name='Course id', help_text='Select Course Id', on_delete=models.CASCADE)
    enrollment_date = models.DateField(
        verbose_name='Coures enrollment date', auto_now_add=True)
    status = models.CharField(max_length=2, choices=StatusChoices.choices,
                              verbose_name='Course Status', help_text='Select student status in the course')

    class Meta:
        ordering = ['enrollment_date', 'couse_id', 'student_id']

    def __str__(self) -> str:
        return "({0}) The student {1}, is enrolled in the course {2} and the status is {3}".format(self.id, self.student_id, self.course_id, self.status)


"""
A class representing the enrollment of a student in a degree program.

Attributes:
    student_id (ForeignKey): The foreign key to the Students model representing the student enrolled in the degree program.
    degree_id (ForeignKey): The foreign key to the Degrees model representing the degree program in which the student is enrolled.
    start_date (DateField): The date when the student enrolled in the degree program.
    end_date (DateField): The date when the student completed the degree program (optional).

Meta:
    ordering (list): A list specifying the default ordering of DegreeEnrollment instances in queries.

Methods:
    __str__(): Returns a string representation of the DegreeEnrollment instance.

"""


class DegreeEnrollment(models.Model):
    student_id = models.ForeignKey(
        Students, verbose_name='Student id', help_text='Select Student Id', on_delete=models.CASCADE)
    degree_id = models.ForeignKey(
        Degrees, verbose_name='Degree id', help_text='Select Degree Id', on_delete=models.CASCADE)
    start_date = models.DateField(
        verbose_name='Degree enrollment date', auto_now_add=True)
    end_date = models.DateField(null=True, blank=True, verbose_name='Degree end date',
                                help_text='Select the date where the student got the degree')

    class Meta:
        ordering = ['id', 'degree_id', 'student_id']

    def __str__(self) -> str:
        return "({0}) The student {1}, is enrolled in {2}".format(self.id, self.student_id, self.degree_id)
