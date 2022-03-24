from email.policy import default
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, fullName, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        return self.create_user(email, fullName, password, **other_fields)

    def create_user(self, email, fullName, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide a valid email address.'))
        email = self.normalize_email(email)
        user = self.model(email=email, fullName=fullName, **other_fields)
        user.set_password(password)
        user.save()
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    userTypes = (("admin", "admin"), ("user", "user"))
    genders = (("M", "male"), ("F", "female"), ("O", "others"))

    fullName = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    image = models.CharField(max_length=255, default=None, null=True)
    password = models.CharField(max_length=255, null=False)
    mobileNo = models.CharField(max_length=255, unique=True, null=True)
    gender = models.CharField(max_length=255, choices=genders, null=True, default="M")
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    userType = models.CharField(max_length=255, choices=userTypes, null=False, default="user")
    otp = models.CharField(max_length=255,null=True)
    is_staff = models.BooleanField(default=False, null=False)
    is_superuser = models.BooleanField(default=False, null=False)
    createdAt = models.DateTimeField(default=now, editable=False)
    updatedAt = models.DateTimeField(default=now, editable=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName']
    objects = CustomAccountManager()

    class Meta:
        db_table = 'users'