from django.contrib import admin

# Register your models here.
from prenotazioni.models import Prenotazione,MovimentiPrenotazione,AnagraficaScuole
from prenotazioni.models import TabellaRuoli,TabellaTurni,TabellaSettori,AnagraficaVideo


admin.site.register(Prenotazione)
admin.site.register(MovimentiPrenotazione)
admin.site.register(AnagraficaScuole)  
admin.site.register(TabellaTurni)
admin.site.register(TabellaSettori)
admin.site.register(TabellaRuoli)
admin.site.register(AnagraficaVideo)
