from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User


class UserManager (BaseUserManager):
    """Helps manage users"""
    def create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        # password needs to be encrypted.
        user.set_password(password)
        print("pass: ", password)
        user.save(using=self._db)
        return user


class Doctor(AbstractBaseUser):
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()  # WHY

    USERNAME_FIELD = 'email'


class Patient (AbstractBaseUser):
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    SEVERE = 'S'
    MODERATE = 'M'
    MILD = 'ML'
    diagnosis = (
        (SEVERE, 'Severe'),
        (MODERATE, 'Moderate'),
        (MILD, 'Mild')
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Appointment(models.Model):
    p_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    d_id = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    
   
