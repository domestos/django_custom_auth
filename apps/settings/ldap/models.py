from django.db import models
from django.core import signing

# Create your models here.
class SingletonModel(models.Model):
    class Meta:
        abstract = True
 
    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)
 
    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


# rename later as LdapCredentials
class LdapSettings(SingletonModel):
    LDAP_URL = models.CharField(max_length=50, default="" )
    LDAP_USER = models.CharField(max_length=30, default="" )
    LDAP_PASS = models.CharField(max_length=30, default="" )
    LDAP_BASE_DN = models.CharField(max_length=250, default="" )
    LDAP_AUTH = models.BooleanField(default='False')
    
    def __str__(self):            
            return self.LDAP_URL
    
    def encrypt_pass(self, raw_pass):
        hash_pass = signing.dumps({"password": raw_pass})
        print(hash_pass)
        return hash_pass


    def decrypt_pass(self, hash_pass):
        raw_pass = signing.loads(hash_pass)
        raw_pass = (raw_pass['password']).encode('utf-8').decode("utf-8")    
        return raw_pass


    def save(self, **kwargs):
        self.LDAP_PASS = self.encrypt_pass(self.LDAP_PASS)
        super(LdapSettings, self).save()

