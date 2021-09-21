from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self,email,gender,first_name,last_name,dob,nationality,password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not gender:
            raise ValueError("User must have gender")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        if not dob:
            raise ValueError("User must have a date of bith")
        if not nationality:
            raise ValueError("User must have a nationality")

        user = self.model(
            email=self.normalize_email(email),
            gender=gender,
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            nationality=nationality
        )
        user.set_password(password)
        user.save(using=self._db)
        return  user


    def create_superuser(self,email,gender,first_name,last_name,dob,nationality,password):
        user = self.create_user(
            email=self.normalize_email(email),
            gender=gender,
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            nationality=nationality,
            password=password
            )

        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user






class UserAccount(AbstractBaseUser):
    CH              =[('F','Female'),('M','Male'),('N','Non binnary')]


    email           =models.EmailField(verbose_name="email",max_length=60,unique=True)
    date_joined     =models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login      =models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=True)
    is_staff        =models.BooleanField(default=False)
    is_superuser    =models.BooleanField(default=False)
    first_name      =models.CharField(max_length=30)
    last_name       =models.CharField(max_length=30)
    gender          =models.CharField(max_length=1,choices=CH)
    dob             =models.DateField(auto_now=False, auto_now_add=False)
    about_me        =models.CharField(max_length=500)
    collage         =models.CharField(max_length=30)
    school          =models.CharField(max_length=30)
    workplace       =models.CharField(max_length=30)
    nationality     =models.CharField(max_length=30)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['gender','first_name','last_name','dob','nationality']
    objects = MyAccountManager()
    def __str__(self):
        return (self.email)

    def has_perm(self,perm,odj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True
