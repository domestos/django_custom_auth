from django.contrib import admin
from .models import LdapSettings
# Register your models here.

class  LdapSettingsAdmin(admin.ModelAdmin):
        # Создадим объект по умолчанию при первом страницы SiteSettingsAdmin со списком настроек
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)        
        # обязательно оберните загрузку и сохранение SiteSettings в try catch,
        # чтобы можно было выполнить создание миграций базы данных
        try:
            config = LdapSettings.load()
            # this check needs becaus method save use encrypt
            if config.LDAP_PASS =='':
                print("== Creating default ldap settings ==")                
                config.save()
        except Exception as e:
            print(e, "== LDAP Settings isn't exist ==")
            pass

#   запрещаем добавление новых настроек
    def has_add_permission(self, request, obj=None):
        return False
 
    # а также удаление существующих
    def has_delete_permission(self, request, obj=None):
        return False
 


admin.site.register(LdapSettings, LdapSettingsAdmin)