 
import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from .models import User
from django.utils.html import format_html
from django.conf import settings

class ImageColumn(tables.Column):
        def render(self, value):
            return format_html(
               '<img src="{url}" class="fav" height="20px", width="20px">',
                url= settings.MEDIA_URL+'/'+str(value)
                )

class UserTable(tables.Table):
    username = tables.LinkColumn("profile_url", args=[A("pk")])
    id = tables.Column(footer="Total:"+str(User.objects.count()))
    image = ImageColumn()    # template_name = "django_tables2/bootstrap.html"
    # tables.LinkColumn(attrs={"a": {"style": "color: red;"})
    class Meta:
        model = User
        template_name = "django_tables2/bootstrap.html"
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'department', 'when_created','when_changed', 'is_active')