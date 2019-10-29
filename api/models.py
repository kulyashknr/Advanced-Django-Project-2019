from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from rest_framework.authtoken.models import Token
from .constraints import USER_ROLES


class MainUser(AbstractUser):
    status = models.CharField(choices=USER_ROLES)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.id}: {self.username}'


class Profile(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    #photo =


class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='company')
    description = models.TextField
    salary = models.IntegerField
    candidates = models.ManyToManyField(MainUser)
    is_active = models.BooleanField()

    def __str__(self):
        return f'{ self.name }: { self.salary }, { self.company }'


class Company(models.Model):
    name = models.CharField(max_length=255)
    hr = models.ForeignKey(MainUser, on_delete=models.CASCADE, null=True, related_name='hr')
    description = models.TextField
    vacancies = models.ManyToManyField(Vacancy)

    def __str__(self):
        return f'{ self.name }: { self.description }'





