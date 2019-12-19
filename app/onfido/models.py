from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(models.Model):

    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'users'
