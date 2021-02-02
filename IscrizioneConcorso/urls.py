"""IscrizioneConcorso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path,re_path
from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateViews
from users.forms import CustomUserForm


from IscrizioneConcorso.views import mailConfermaPrenotazione,visualizzaprivacy,dataPrenotazioneModificata
from IscrizioneConcorso.views import visualizzaGuidaUtente,mailInformativa,visualizzaPagamenti
from IscrizioneConcorso.views import mailReset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mail-informativa/<int:pk>/', mailInformativa, name='mail_informativa'),
    path('mail-reset/<str:email>', mailReset, name='mail_reset'),
    path('mail-conferma-prenotazione/<int:pk>/', mailConfermaPrenotazione, name='mail_conferma_prenotazione'),
    path('data-prenotazione-modificata/<int:pk>/', dataPrenotazioneModificata, name='data_prenotazione_modificata'),
    path('privacy/', visualizzaprivacy,name='run_visualizzaprivacy'),
    path('pagamentiy/', visualizzaPagamenti,name='visualizza_pagamenti'),
    path('guidautente/', visualizzaGuidaUtente,name='guida_utente'),
#    path('accounts/register/', RegistrationView,name='django_registration_register'),



    path("accounts/register/",
         RegistrationView.as_view(
            form_class=CustomUserForm,
            success_url="/",
         ), name="django_registration_register"),



    path('api/', include("users.api.urls")),
    path('api/', include("prenotazioni.api.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('api-auth/',include("rest_framework.urls")),
    path('api/rest-auth/',include("rest_auth.urls")),
    path('api/rest-auth/registration/',include("rest_auth.registration.urls")),
    re_path(r'^.*$',IndexTemplateViews.as_view(),name='entry-point')
]
