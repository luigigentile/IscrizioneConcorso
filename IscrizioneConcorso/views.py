
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponseBadRequest,HttpResponse
from prenotazioni.models import Prenotazione,MovimentiPrenotazione
from users.models import CustomUser
from users.forms import CustomUserForm

#def RegistrationView(request):
#    success_url="/"
#    form_class=CustomUserForm,
#
#    return HttpResponseRedirect(success_url)
#
#
##    return render(request)
##    return render(request,"127.0.0.1:8000/IscrizioneConcorso/frontend/views/userEditor.vue")








def mailConfermaPrenotazione(request,pk):
    import os
    EMAIL_HOST_PASSWORD=os.getenv('EMAIL_HOST_PASSWORD')
#    print("pk= " + str(pk))
    prenotazione = Prenotazione.objects.get(pk=pk)
    print("User Id della prenotazione = " + str(prenotazione.user.id))
    user = CustomUser.objects.get(id=prenotazione.user.id)
#    dettagliPrenotazione = MovimentiPrenotazione.objects.get(prenotazione=prenotazione.id)
    dettagliPrenotazione = MovimentiPrenotazione.objects.filter(prenotazione=prenotazione.id)
#    print(user.email)
#    print(request.user.email)
    success_url="/"
    destinatari = (user.email,)
#   CONTENUTO DELLA MAIL
    contenuto = "Gentile " + user.first_name  + ", grazie per esserti iscritto alla mostra di  Sperimentando\n\n"
    contenuto = contenuto + "Utente              " + str(user.username) + "\n"
    contenuto = contenuto + "Scuola/Gruppo:      " + str(prenotazione.nome_scuola) + "\n"
    contenuto = contenuto + "N.ro accompagnatori:" + str(prenotazione.numero_accompagnatori) + "\n"
    contenuto = contenuto + "N.ro alunni:        " + str(prenotazione.numero_totale_alunni) + "\n"
    contenuto = contenuto + "Data Prenotazione:  " + str(prenotazione.data_prenotazione) + "\n"
    contenuto = contenuto + "Esigenze:           " + str(prenotazione.esigenze) + "\n\n"
#   DETTAGLI PRENOTAZIONE
    contenuto = contenuto + "Dettaglio Prenotazione:" + "\n"
    contenuto = contenuto + "Settore\t" + "Orario\t\t" + "Classe\t" +"N.ro Alunni\t" +"\n"

    for dettaglio in dettagliPrenotazione:
        contenuto = contenuto + str(dettaglio.turno.settore) + "\t"
        contenuto = contenuto + str(dettaglio.turno.orario_turno) + "\t "
        contenuto = contenuto + str(dettaglio.classe) + "\t"
        contenuto = contenuto + str(dettaglio.numero_alunni) + "\t"
        contenuto = contenuto +  "\n"

    print(contenuto)
    print(destinatari)

    from django.core.mail import EmailMessage
    email = EmailMessage(subject='Ti sei iscritto correttamente ', body=contenuto, to=destinatari)
    email.send()

#    success_url = reverse_lazy('home')
    return HttpResponseRedirect(success_url)
#    return HttpResponseRedirect('/')


#    return render(request)
#    return render(request,"powerSimulation/simulazioneResults.html",context)


def dataPrenotazioneModificata(request,pk):
#   SELEZIONA  LA PRENOTAZIONE CON id=pk
    prenotazione = Prenotazione.objects.get(pk=pk)
#   SELEZIONA  IL DETTAGLIO DELLE PRENOTAZIONI
    dettagliPrenotazione = MovimentiPrenotazione.objects.filter(prenotazione=prenotazione.id)
#   ELIMINA IL DETTAGLIO DELLE PRENOTAZIONI
    for dettaglio in dettagliPrenotazione:
        dettaglio.delete()
#    RITORNA ALLA PAGINA INIZIALE
    success_url="/"
    return HttpResponseRedirect(success_url)


def visualizzaprivacy(request):

    #    email.send()
#    print(request.user.email)
    print("run e-mail sended ")
#    success_url = reverse_lazy('127.0.0.1:8000/IscrizioneConcorso/privacypolicy.html/')
#    return HttpResponseRedirect(success_url)

#    return HttpResponseRedirect('https://sperimentandoaps.wordpress.com/informativa-privacy/')

#    return HttpResponseRedirect('/')

#    return render(request)
    return render(request,"https://sperimentandoaps.wordpress.com/informativa-privacy/")
