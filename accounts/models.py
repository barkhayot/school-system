from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator


class AccountManager(BaseUserManager):
    def create_user(self, email, account_id, first_name, last_name, username, password=None):
        if not email:
            raise ValueError("User must have an email")

        if not username:
            raise ValueError("User must have a username")

        if not account_id:
            raise ValueError("User must have an account ID")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            account_id = account_id,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_professor(self, email, account_id, first_name, last_name, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            account_id = account_id,
        )

        user.is_professor = True
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, account_id, first_name, last_name, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            account_id = account_id,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser =True

        user.save(using=self._db)
        
        return user



class Account(AbstractBaseUser):
    account_id      = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)

    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_superuser    = models.BooleanField(default=False)

    is_professor    = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['account_id', 'username', 'first_name', 'last_name']


    objects = AccountManager()

    def __int__(self):
        return self.account_id

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
