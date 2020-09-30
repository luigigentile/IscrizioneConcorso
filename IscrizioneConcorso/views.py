
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponseBadRequest,HttpResponse

def eseguimail(request):

    from django.core.mail import EmailMessage
    email = EmailMessage('Hello', 'World', to=['iscrizionisperimentando@gmail.com'])
#    email.send()
    print(request.user.email)
    print("run e-mail sended ")
#    success_url = reverse_lazy('home')
#    return HttpResponseRedirect(success_url)
    return HttpResponseRedirect('/')


#    return render(request)
#    return render(request,"powerSimulation/simulazioneResults.html",context)
