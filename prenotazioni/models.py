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
        return str(self.id) + " " + str(self.data) + " " + str(self.settore) + " " + str(self.orario_turno)

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turni'

class StatusPrenotazione(models.TextChoices):
    DACONFERMARE = 'DC', 'Da Confermare'
    CONFERMATO = 'CO', 'Confermato'

class Prenotazione(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    data_prenotazione = models.DateField()
    status = models.CharField(
        max_length=2,
        choices=StatusPrenotazione.choices,
        default=StatusPrenotazione.DACONFERMARE,
        null=True
    )


    scuola = models.BooleanField(default=False,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete = models.CASCADE,
                                related_name = 'prenotazioni')
    nome_scuola = models.CharField(max_length=50,null=True)
    numero_accompagnatori = models.PositiveIntegerField(default=2)
    numero_totale_alunni = models.PositiveIntegerField(null=True)
    esigenze = models.TextField(blank=True, null=True)
    pagato = models.BooleanField(default=False,null=True)

    def __str__(self):
        return str(self.id) + " " + str(self.user) + " " + str(self.data_prenotazione)

    class Meta:
        verbose_name = 'Prenotazione'
        verbose_name_plural = 'Prenotazioni'

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
    numero_alunni = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + " " + str(self.turno) + " " + str(self.classe)

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
