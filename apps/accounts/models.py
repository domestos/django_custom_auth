from django.db import models
from django.urls import reverse
from django.utils import timezone
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import AbstractUser
# Create your models here.


class NullableEmailField(models.EmailField):
    """ 
    This Class allows save unique email and Null to DataBase
    """
    description = "EmailField that stores NULL but returns ''"
    __metaclass__ = models.Field
    def to_python(self, value):
        if isinstance(value, models.EmailField):
            return value
        return value or ''
    def get_prep_value(self, value):
        return value or None

class User(AbstractUser):
    email = NullableEmailField(('e-mail address'),  blank=True, null=True, default=None, unique=True)
    when_created = models.DateTimeField(default=timezone.now , blank=True)
    when_changed = models.DateTimeField( default=timezone.now, blank=True)
    ldap_user = models.BooleanField(default=False)
    department = models.CharField(max_length=150, blank=True)
    # mobile_phone = 
    image = models.ImageField(upload_to='profile\photo', blank=True, default='asset\placeholder-profile.jpg')
    # history = HistoricalRecords(related_name='history_profile')

    def __str__(self):
        return "{}".format(self.username)


    # @property
    # def action(self):
    #     return "Edit"


    def get_absolute_url(self):
        return reverse("user_detail_url", kwargs={'pk':self.pk} )
