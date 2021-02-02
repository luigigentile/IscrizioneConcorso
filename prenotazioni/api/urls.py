from django.urls import include, path
from rest_framework.routers import DefaultRouter
from prenotazioni.api import views as qv

router = DefaultRouter()
router.register(r"prenotazioni", qv.PrenotazioniViewSet)
router.register(r"turni", qv.TurniViewSet)
router.register(r"settori", qv.SettoriViewSet)
router.register(r"ruoli", qv.RuoliViewSet)
router.register(r"movimentiPrenotazioni", qv.MovimentiPrenotazioneViewSet)
router.register(r"scuole", qv.AnagraficaScuoleViewSet)
router.register(r"video", qv.AnagraficaVideoViewSet)

urlpatterns = [
    path("", include(router.urls)),
#    path("prenotazioni/<int:pk>/movimenti/", qv.PrenotazioniMovimentiListAPIView.as_view(),name='elenco-movimenti-prenotazione'),
    path("prenotazione/<int:pk>/movimenti/", qv.PrenotazioneMovimentiListAPIView.as_view(),name='elenco-movimenti-prenotazione'),
    path("prenotazioni/<int:pk>/movimento/", qv.MovimentiPrenotazioneCreateAPIView.as_view(),name='crea-movimento-prenotazione'),
    path("distinctdataturni/", qv.DistinctDataTurni.as_view(),name='distinct-data-turni'),
    path("distinctdataprenotazione/", qv.DistinctDataPrenotazione.as_view(),name='distinct-data-prenotazione'),
    path('anagraficascuole/deleteall/', qv.anagraficaScuoleDeleteAll.as_view(),name = 'scuole-Delete-All'),
    path('listaturni/', qv.ListaTurni.as_view(),name = 'turni-list'),
    path('listaprenotazioni/', qv.ListaPrenotazioni.as_view(),name = 'prenotazioni-list'),
]
