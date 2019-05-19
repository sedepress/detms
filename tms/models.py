from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    user = models.ManyToManyField(User, through='UserCompany')

    def __str__(self):
        return self.name

class UserCompany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tms_user_company'

class Project(models.Model):
    name = models.CharField(max_length=128, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(default=0)
    user = models.ManyToManyField(User, through='UserProject')

    def __str__(self):
        return self.name

class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tms_user_project'