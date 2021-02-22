
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponseBadRequest,HttpResponse
from prenotazioni.models import Prenotazione,MovimentiPrenotazione
from users.models import CustomUser
from users.forms import CustomUserForm
from django.conf import settings

#def RegistrationView(request):
#    success_url="/"
#    form_class=CustomUserForm,
#
#    return HttpResponseRedirect(success_url)
#
#
##    return render(request)
##    return render(request,"127.0.0.1:8000/IscrizioneConcorso/frontend/views/userEditor.vue")

def visualizzaGuidaUtente(request):
    with open(settings.BASE_DIR + '/static/GuidaUtente.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read())
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        response['Content-Disposition'] ="attachment; filename=GuidaUtente.pdf"
        return response
    pdf.closed
#

def mailConfermaPrenotazione(request,pk):
    import os
    prenotazione = Prenotazione.objects.get(pk=pk)
    #print("User Id della prenotazione = " + str(prenotazione.user.id))
    user = CustomUser.objects.get(id=prenotazione.user.id)
    dettagliPrenotazione = MovimentiPrenotazione.objects.filter(prenotazione=prenotazione.id)
#    print(request.user.email)
    success_url="/"
    destinatari = (user.email,)
    perConoscenza = (settings.DEFAULT_FROM_EMAIL,)
    if (user.first_name) :
        name=user.first_name
    else:
        name = user.username
      
#   CONTENUTO DELLA MAIL
    contenuto = "Gentile " + name  + ", \ngrazie per aver scelto di visitare la Mostra Sperimentando.\n"
    contenuto = contenuto + "La prenotazione della visita alla mostra è confermata.\n"
    contenuto = contenuto + "Ecco i dettagli della visita:\n"
    contenuto = contenuto + "Utente:                 \t" + str(user.username) + "\n"
    if (prenotazione.scuola): 
        contenuto = contenuto + "Scuola/Gruppo:           \t" + str(prenotazione.nome_scuola) + "\n"
        contenuto = contenuto + "N.ro accompagnatori:    \t" + str(prenotazione.numero_accompagnatori) + "\n"
        contenuto = contenuto + "N.ro alunni:             \t" + str(prenotazione.numero_totale_alunni) + "\n"
        contenuto = contenuto + "Data Prenotazione:       \t" + str(prenotazione.data_prenotazione.strftime('%d-%m-%Y')) + "\n"
    else:
        contenuto = contenuto + "Data Prenotazione:       \t" + str(prenotazione.data_prenotazione.strftime('%d-%m-%Y')) + "\n"
        contenuto = contenuto + "Ora  Prenotazione        \t" + str(prenotazione.ora_prenotazione) + "\n"
        contenuto = contenuto + "N.ro Persone:            \t" + str(prenotazione.numero_accompagnatori) + "\n"
    
    contenuto = contenuto + "Argomenti Preferiti:     \t" + str(prenotazione.argomentiPreferiti) + "\n"
    contenuto = contenuto + "Esigenze:                \t" + str(prenotazione.esigenze) + "\n\n"
    contenuto = contenuto + "Lo Staff di Sperimentando" +"\n"
#   DETTAGLI PRENOTAZIONE
    contenuto = contenuto + "Dettaglio Prenotazione:" + "\n"
    contenuto = contenuto + "Settore\t" + "Orario\t" + "Classe\t\t" +"N.ro Alunni" +"\n"

    for dettaglio in dettagliPrenotazione:
        contenuto = contenuto + str(dettaglio.turno.settore) + "\t\t"
        contenuto = contenuto + str(dettaglio.turno.orario_turno) + "\t\t"
        contenuto = contenuto + str(dettaglio.classe) + "\t\t"
        contenuto = contenuto + str(dettaglio.numero_alunni)
        contenuto = contenuto +  "\n"
    oggetto = "Conferma di prenotazione alla Mostra Sperimentando"
    #print(contenuto)
    #print(destinatari)
    #print(perConoscenza)
    #print(oggetto)
    

    from django.core.mail import EmailMessage
    email = EmailMessage(subject=oggetto, body=contenuto, to=destinatari,bcc=perConoscenza)
    email.send()

  
    return HttpResponseRedirect(success_url)
#    return render(request,"powerSimulation/simulazioneResults.html",context)


def mailInformativa(request,pk):
    import os
    prenotazione = Prenotazione.objects.get(pk=pk)
#   print("User Id della prenotazione = " + str(prenotazione.user.id))
    user = CustomUser.objects.get(id=prenotazione.user.id)
#    print(user.email)
#    print(request.user.email)
    success_url="/"
    destinatari = (user.email,)
    perConoscenza = (settings.DEFAULT_FROM_EMAIL,)
    if (user.first_name) :
        name=user.first_name
    else:
        name = user.username
#   CONTENUTO DELLA MAIL
    if(prenotazione.scuola):
        contenuto = "Gentile " + name  + ", \nGrazie per aver prenotato la visita alla Mostra Sperimentando.\n"
        contenuto = contenuto + "Attenzione: ricordati di pagare e di inviare la ricevuta del pagamento!\n"
        contenuto = contenuto + "Tutte le informazioni per procedere al pagamento sono al seguente indirizzo:\n"
        contenuto = contenuto + "https://sperimentandoaps.wordpress.com/pagamenti-mostra-20-21/\n"
        contenuto = contenuto + "\nRiceverai una mail di conferma della prenotazione da info@aifpadova.it, solo quando riceveremo\n"
        contenuto = contenuto + "la ricevuta di pagamento all’indirizzo mail visitesperimentando@gmail.com.\n"
        contenuto = contenuto + "\n Grazie, \n" 
        contenuto = contenuto + "Lo Staff di Sperimentando" +"\n"

    if(not prenotazione.scuola):
        contenuto = "Gentile " + name  + ", \nGrazie per aver prenotato la visita alla Mostra Sperimentando.\n"
        contenuto = contenuto +  "Attenzione !!\n"
        contenuto = contenuto + "\nSe hai prenotato la visita in presenza, riceverai una mail di conferma della prenotazione da info@aifpadova.it e potrai eseguire il pagamento direttamente alla cassa.\n"
        contenuto = contenuto + "\nSe hai prenotato la visita virtuale, ti verrà inviata una mail di conferma della prenotazione da info@aifpadova.it "
        contenuto = contenuto + "solo quando riceveremo la ricevuta di pagamento all’indirizzo mail visitesperimentando@gmail.com.\n"
        contenuto = contenuto + "Tutte le informazioni per procedere al pagamento sono al seguente indirizzo:\n"
        contenuto = contenuto + "https://sperimentandoaps.wordpress.com/pagamenti-mostra-20-21/.\n"
        contenuto = contenuto + "\nGrazie, \n" 
        contenuto = contenuto + "Lo Staff di Sperimentando" +"\n"

    oggetto = "Informazioni prenotazione per la visita della mostra Sperimentando"
   
    from django.core.mail import EmailMessage
    email = EmailMessage(subject=oggetto, body=contenuto, to=destinatari,bcc=perConoscenza)
    email.send()
   
    #print(oggetto)
    #print(destinatari)
    #print(perConoscenza)
    #print(contenuto)
   

  
    return HttpResponseRedirect(success_url)


def dataPrenotazioneModificata(request,pk):
#   SELEZIONA  LA PRENOTAZIONE CON id=pk
    prenotazione = Prenotazione.objects.get(pk=pk)
#   SELEZIONA  IL DETTAGLIO DELLE PRENOTAZIONI
    dettagliPrenotazione = MovimentiPrenotazione.objects.filter(prenotazione=prenotazione.id).order_by("id")
#   ELIMINA IL DETTAGLIO DELLE PRENOTAZIONI
    for dettaglio in dettagliPrenotazione:
        dettaglio.delete()
#    RITORNA ALLA PAGINA INIZIALE
    success_url="/"
    return HttpResponseRedirect(success_url)


def visualizzaPagamenti(request):
    return render(request,"https://sperimentandoaps.wordpress.com/pagamenti-mostra-20-21/")

def visualizzaprivacy(request):
    #    email.send()
#    print(request.user.email)
   
#    return render(request)
    return render(request,"https://sperimentandoaps.wordpress.com/informativa-privacy/")


def mailReset(request,email):
    print(email)
  
    success_url="/login"
    destinatari = list(email)
#   CONTENUTO DELLA MAIL
    contenuto = "Per Confermare la prenotazione bisogna che lei effettui il pagamento di XXXX€... entro il  gg-mm-aa .\n"
    contenuto = contenuto + "Questo è il link alla sezione dei pagamenti:\n"
    contenuto = contenuto + "https://sperimentandoaps.wordpress.com/pagamenti-mostra-20-21/:\n"
   #
    print(contenuto)
    #print(destinatari)
    oggetto = "Informativa sulla  Mostra Sperimentando"

    from django.core.mail import EmailMessage
    email = EmailMessage(subject=oggetto, body=contenuto, to=destinatari)
   # email.send()
    return HttpResponseRedirect(success_url)
