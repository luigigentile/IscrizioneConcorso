from django.db import models
# Create your models here.
from django.conf import settings

class TabellaRuoli(models.Model):
    ruolo = models.CharField(max_length=30,unique = True)

    def __str__(self):
        return str(self.id) + " " + str(self.ruolo)
    class Meta:
        verbose_name = 'ruolo'
        verbose_name_plural = 'ruoli'


class TabellaSettori(models.Model):
    settore = models.CharField(max_length=30,unique = True)

    def __str__(self):
        return str(self.id) + " " + str(self.settore)
    class Meta:
        verbose_name = 'Settore'
        verbose_name_plural = 'Settori'


class TabellaTurni(models.Model):
    data = models.DateField()
    orario_turno = models.CharField(max_length=30)
    settore = models.ForeignKey(TabellaSettori,
                                on_delete = models.CASCADE,
                                related_name = 'settori')
    numero_posti_disponibili = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return  str(self.id) + " - " + str(self.data.strftime('%d/%m/%Y')) + " - " + str(self.settore) + " - " + str(self.orario_turno)

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turni'

class StatusPrenotazione(models.TextChoices):
    DACONFERMARE = 'DC', 'Da Confermare'
    CONFERMATO = 'CO', 'Confermato'
    EFFETTUATA = 'EF', 'Effettuata'

class TipoVisita(models.TextChoices):
    VIRTUALE = 'VI', 'Virtuale'
    INPRESENZA = 'PR', 'In Presenza'
    

class AnagraficaVideo(models.Model):
    titolo = models.CharField(max_length=50,blank=True)
    descrizione = models.CharField(max_length=250,blank=True)
    note = models.CharField(max_length=250,blank=True)
    collegamento = models.CharField(max_length=128,blank=True)
    settore = models.ForeignKey(TabellaSettori,
                                on_delete = models.CASCADE,
                                related_name = 'settorivideo')
  
    def __str__(self):
        return str(self.id) + " " + str(self.descrizione)
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'video'


class Prenotazione(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    data_prenotazione = models.DateField()
    ora_prenotazione = models.TimeField(null=True,blank = True)
    status = models.CharField(
        max_length=2,
        choices=StatusPrenotazione.choices,
        default=StatusPrenotazione.DACONFERMARE,
        null=True
    )
    tipoVisita = models.CharField(
        max_length=2,
        choices=TipoVisita.choices,
        default=TipoVisita.VIRTUALE,
        null=True
    )


    scuola = models.BooleanField(default=True,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete = models.CASCADE,
                                related_name = 'prenotazioni')
    nome_scuola = models.CharField(max_length=50,null=True,blank=True)
    numero_accompagnatori = models.PositiveIntegerField(default=1)
    numero_totale_alunni = models.PositiveIntegerField(null=True)
    esigenze = models.TextField(blank=True, null=True)
    pagato = models.BooleanField(default=False,null=True)
    argomentiPreferiti = models.CharField(max_length=250,blank=True, null=True)
    mailInformativaInviata = models.BooleanField(default=False,null=True)
    mailConfermaInviata = models.BooleanField(default=False,null=True)
   

    def __str__(self):
        return str(self.id) + " - " + str(self.user) + " - " + str(self.data_prenotazione.strftime('%d/%m/%Y'))

    class Meta:
        verbose_name = 'Prenotazione'
        verbose_name_plural = 'Prenotazioni'
    
    @property
    def labelStatus(self):
        return StatusPrenotazione(self.status).label

class MovimentiPrenotazione(models.Model):
    prenotazione = models.ForeignKey(Prenotazione,
                                on_delete = models.CASCADE,
                                related_name = 'movimenti_prenotazione')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    turno = models.ForeignKey(TabellaTurni,
                                on_delete = models.CASCADE,
                                null=True,
                                related_name = 'turni')
    classe = models.CharField(max_length=30,blank=True, null=True)
    numero_alunni = models.PositiveIntegerField(blank=True, default=0)
  
    orario_turno = models.CharField(max_length=30,null=True)
    settore = models.CharField(max_length=31,null = True)
    orario = models.CharField(max_length=30,null=True)
    

    def __str__(self):
        return str(self.id) + " -  " + str(self.turno) + " " + str(self.classe)

    class Meta:
        verbose_name = 'Dettaglio Prenotazione'
        verbose_name_plural = 'Dettaglio Prenotazioni'







class AnagraficaScuole(models.Model):
    codice_ministeriale = models.CharField(primary_key=True,max_length=10)
    nome_scuola = models.CharField(max_length=50)
    indirizzo = models.CharField(max_length=50,blank=True)
    comune = models.CharField(max_length=50,blank=True)
    sigla = models.CharField(max_length=6,blank=True)
    provincia = models.CharField(max_length=50,blank=True)
    tiposcuola = models.CharField(max_length=50,blank=True)
    telefono = models.CharField(max_length=40,blank=True)

    def __str__(self):
        return str(self.nome_scuola)

    class Meta:
        verbose_name = 'scuola'
        verbose_name_plural = 'scuole'


