from django.conf.urls import url
from django.conf.urls import include
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete, password_change_done
)

#alle URLs die aufrubar sind, werden hier aufgelistet. Die views-Funktionen werden hiermit aufgerufen

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'benutzeraccounts/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
]
