"""
Django authentication backend.
"""

from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from .ldap import *
from apps.settings.ldap.models import LdapSettings


import logging
logger = logging.getLogger(__name__)

class LDAPBackend(ModelBackend):

    logger.info("Run backend LDAP AUTH")
    """
    An authentication backend that delegates to an LDAP
    server.

    User models authenticated with LDAP are created on
    the fly, and syncronised with the LDAP credentials.
    """

    def is_enabled_ldap_auth(self):
        """
        Return True if LDAP Auth is Enabled
        """
        try:
            return LdapSettings.objects.all().first().LDAP_AUTH
        except Exception as e:
            logger.info("Exception:::", str(e))
            return False


    def authenticate(self, *args, **kwargs):
        #need       
        if self.is_enabled_ldap_auth():
            return authenticate(*args, **kwargs)
        else:
            logger.info("LDAP AUTH is Disabled")
            return None

