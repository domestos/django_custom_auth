""" ACCOUNTS URL """

from django.contrib import admin
from django.urls import path
from django.views import View
from .views import AccountsView


from django.conf.urls import url

from .views import *

urlpatterns = [
    path('', AccountsView.as_view(), name='accounts_url'   ),
    
    url(r'^signup/$', signup, name='signup'),
    # url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    # url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    # url(r'^admin/', admin.site.urls),
]
