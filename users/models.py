from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager

class UserprofileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        email = email.lower() 

        user = self.model(
            email=email,
            name=name
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_realtor(self,email,name,password=None):
        user = self.create_user(email,name,password)
        user.is_realtor = True
        user.save()
        return user
    
    def create_superuser(self,email,name,password=None):
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class Userprofile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_realtor = models.BooleanField(default=False)

    objects =UserprofileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name",]

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "UserProfile"
# Create your models here.


# Create your models here.
