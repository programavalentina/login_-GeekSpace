from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.utils import datetime_safe
from django.utils.translation import ugettext_lazy as _

class UserType(models.Model):
    LicenceType = models.AutoField(primary_key=True)
    Description = models.TextField()

class UserManager(BaseUserManager):

    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):

        if not username:
            raise ValueError('Usuarios deben Tener un nombre de usuario valido.')

        usuario = self.model(
            username=username,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = True,
            last_login = datetime_safe.datetime.now(),
            date_joined = datetime_safe.datetime.now(),
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, True, **extra_fields)

class User(AbstractBaseUser):
    Licence = models.AutoField('Licence Student', primary_key=True)
    username = models.CharField("Username", max_length=50, unique=True)
    Name1 = models.CharField("Name", max_length=50)
    Name2 = models.CharField(max_length=50,blank=True,null=True)
    Name3 = models.CharField(max_length=50,blank=True,null=True)
    LastName1 =models.CharField(max_length=50,blank=True)
    LastName2 = models.CharField(max_length=50,blank=True,null=True)
    BirthDate = models.DateField('Birth Name',null=True)
    Email = models.EmailField(max_length=80,null=True)
    Phone = models.PositiveIntegerField('Contact Phone', blank=True, null=True)
    FKLicenceType = models.ForeignKey(UserType, on_delete=models.CASCADE, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.nombre, self.apellido)
        return full_name.strip()

    def get_short_name(self):
        return self.nombre

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Course(models.Model):
    IdCourse = models.AutoField(primary_key=True)
    NameCourse = models.CharField(max_length=45)
    Description = models.TextField()
    Teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class ListStudents(models.Model):
    FKIdCourse = models.ManyToManyField(Course)
    FKLicence = models.ManyToManyField(User)

class Assistance(models.Model):
    FKLicence = models.ForeignKey(User, on_delete=models.CASCADE)
    Estate = models.BooleanField('1 Assistence; 0 No Assistence', default=False)