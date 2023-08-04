from django.db import models


class GenderChoices(models.TextChoices):
    MALE = ("male", "Male")
    FEMALE = ("female", "Female")


class Subject(models.Model):
    name = models.CharField(max_length=125, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Group(models.Model):
    name = models.CharField(max_length=125, unique=True)
    subjects = models.ManyToManyField(Subject, related_name="subjects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    firstname = models.CharField(max_length=125)
    lastname = models.CharField(max_length=125)
    phone_number = models.CharField(max_length=13, unique=True)
    group = models.ForeignKey(Group, related_name="student_group", on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=125, choices=GenderChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ["lastname", "lastname"]

    def __str__(self):
        return f"{self.firstname} {self.lastname}"





class Employee(models.Model):
    firstname = models.CharField(max_length=125)
    lastname = models.CharField(max_length=125)
    department = models.CharField(max_length=13)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=125, choices=GenderChoices.choices)
    profession = models.CharField(max_length=125)
    branch = models.CharField(max_length=543)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ["firstname", "lastname"]

    def __str__(self):
        return f"{self.firstname} {self.lastname}"