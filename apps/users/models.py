from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from PIL import Image as Img

from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


class Personajuridica(models.Model):
    razon_social = models.CharField(max_length=100)
    nit = models.BigIntegerField()
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    telefono2 = models.IntegerField(null=True, blank=True)
    telefono3 = models.IntegerField(null=True, blank=True)
    departamento = models.CharField(max_length=100)
    municipios = models.CharField(max_length=100)

    def __unicode__(self):
        return self.razon_social

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        email = self.normalize_email(email)
        if not email:
            raise ValueError('El email debe ser obligatorio')
        user = self.model(username=username, email=email, is_active=True,
                          is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    nombre = models.CharField(max_length=200)
    p_apellido = models.CharField(max_length=100)
    s_apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField(null=True, blank=True)
    # avatar = models.ImageField(upload_to='users')
    avatar = ProcessedImageField(upload_to='users',
                                           processors=[ResizeToFill(300, 300)],
                                           format='JPEG',
                                           options={'quality': 60})
    empresa = models.ForeignKey(Personajuridica, null=True)

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username

    # def save(self, *args, **kwargs):
    #     if self.avatar:
    #         image = Img.open(StringIO.StringIO(self.avatar.read()))
    #         image.thumbnail((350, 350), Img.ANTIALIAS)
    #         output = StringIO.StringIO()
    #         image.save(output, format='JPEG', quality=75)
    #         output.seek(0)
            
    #     super(User, self).save(*args, **kwargs)
