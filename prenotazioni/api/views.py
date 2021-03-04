from django.shortcuts import get_object_or_404

from rest_framework import generics,status,viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import  IsAuthenticated,AllowAny
from rest_framework.response import  Response
from rest_framework.views import  APIView

from prenotazioni.api.serializers import MovimentiPrenotazioneSerializer, PrenotazioneSerializer
from prenotazioni.api.serializers import TurniSerializer,DataTurniSerializer,SettoriSerializer
from prenotazioni.api.serializers import DataPrenotazioniSerializer,AnagraficaScuoleSerializer
from prenotazioni.api.serializers import AnagraficaVideoSerializer
from prenotazioni.api.serializers import TabellaRuoliSerializer,ListaTurniSerializer


from prenotazioni.api.permissions import IsUserOrReadOnly,IsOwnerOrReadOnly,IsUserOrReadOnlyOrIsStaff
from prenotazioni.models import TabellaTurni,TabellaSettori,TabellaRuoli

from prenotazioni.models import Prenotazione,MovimentiPrenotazione,AnagraficaScuole,AnagraficaVideo
from rest_framework.filters import SearchFilter,OrderingFilter

class PrenotazioniViewSet(viewsets.ModelViewSet):
    queryset = Prenotazione.objects.all().order_by("-created_at")
    serializer_class = PrenotazioneSerializer
    permission_classes = [IsUserOrReadOnlyOrIsStaff]
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['data_prenotazione','status']
    ordering_fields = ['data_prenotazione','id']

    def get_queryset(self):
#        username = self.request.query_params.get('username', None)
        user = self.request.user
        if (user.is_staff):
            return Prenotazione.objects.all().order_by("-data_prenotazione")
        else:
            return Prenotazione.objects.filter(user=user).order_by("-created_at")



    def perform_create(self, serializer):
#        print(f"numero sessioniin in perfom create  = {self.request.session['num_visits']}" )
#        print(self.request.session.get_expire_at_browser_close())
#        print(self.request.session.keys() )
#        print(self.request.session.items())
#        print(self.request.user)
#        print(self.request.data)
##        request.session.get('num_visits', 0)
        serializer.save(user=self.request.user)


class ListaPrenotazioni(generics.ListAPIView):
    queryset = Prenotazione.objects.all().order_by("-created_at")
    serializer_class = PrenotazioneSerializer
    permission_classes = [IsAuthenticated]



class MovimentiPrenotazioneViewSet(viewsets.ModelViewSet):
    queryset = MovimentiPrenotazione.objects.all().order_by("id")
    serializer_class = MovimentiPrenotazioneSerializer
    permission_classes = [IsAuthenticated]


class MovimentiPrenotazioneCreateAPIView(generics.CreateAPIView):
    queryset = MovimentiPrenotazione.objects.all()
    serializer_class =  MovimentiPrenotazioneSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
        request_user =self.request.user
        kwarg_pk = self.kwargs.get('pk')
        print(kwarg_pk)
        prenotazione = get_object_or_404(Prenotazione,pk=kwarg_pk)
        if (prenotazione.user !=  request_user) :
            raise ValidationError("Utente non abilitato")
        serializer.save(prenotazione=prenotazione)



class PrenotazioneMovimentiListAPIView(generics.ListAPIView):
    serializer_class =  MovimentiPrenotazioneSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_pk = self.kwargs.get('pk')
        prenotazione = get_object_or_404(Prenotazione,pk=kwarg_pk)
        return MovimentiPrenotazione.objects.filter(prenotazione=prenotazione)

class MovimentoPrenotazioneRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=MovimentiPrenotazione.objects.all()
    serializer_class =  MovimentiPrenotazioneSerializer
    permission_classes = [IsAuthenticated]


class TurniViewSet(viewsets.ModelViewSet):
    queryset = TabellaTurni.objects.all().order_by("id")
    serializer_class = TurniSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ["data"]
    ordering_fields = ['id','numero_posti_disponibili','data']


class ListaTurni(generics.ListAPIView):
    queryset = TabellaTurni.objects.all().order_by("id")
    serializer_class = ListaTurniSerializer
    permission_classes = [IsAuthenticated]


class DataTurni(generics.ListAPIView):
    serializer_class =  TabellaRuoliSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        from django.db.models import Count
#        queryset = TabellaTurni.objects.annotate(Count('data'))

        query_set = TabellaTurni.objects.distinct()
        return query_set

class DistinctDataTurni(generics.ListAPIView):
    serializer_class =  DataTurniSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        from django.db.models import Count
#        query_set = TabellaTurni.objects.annotate(Count('data'))
#        query_set = TabellaTurni.objects.values('data').annotate(name_count=Count('data')).filter(name_count=3)
        query_set = TabellaTurni.objects.values('data').order_by('data').annotate(name_count=Count('data'))
        return query_set

class DistinctDataPrenotazione(generics.ListAPIView):
    serializer_class =  DataPrenotazioniSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        from django.db.models import Count
#        query_set = TabellaTurni.objects.annotate(Count('data'))
#        query_set = TabellaTurni.objects.values('data').annotate(name_count=Count('data')).filter(name_count=3)
        query_set = Prenotazione.objects.values('data_prenotazione').annotate(name_count=Count('data_prenotazione')).order_by('data_prenotazione')
        return query_set


class SettoriViewSet(viewsets.ModelViewSet):
    queryset = TabellaSettori.objects.all().order_by("id")
    serializer_class = SettoriSerializer
    permission_classes = [IsAuthenticated]


class AnagraficaScuoleViewSet(viewsets.ModelViewSet):
    queryset = AnagraficaScuole.objects.all().order_by("sigla")
    serializer_class = AnagraficaScuoleSerializer
    permission_classes = [IsAuthenticated]


class AnagraficaVideoViewSet(viewsets.ModelViewSet):
    queryset = AnagraficaVideo.objects.all().order_by("settore")
    serializer_class = AnagraficaVideoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['settore']
    ordering_fields = ['settore']
   


class RuoliViewSet(viewsets.ModelViewSet):
    queryset = TabellaRuoli.objects.all().order_by("ruolo")
    serializer_class = TabellaRuoliSerializer
    permission_classes = [IsAuthenticated]



class anagraficaScuoleDeleteAll(APIView):

    def delete(self, request,  format=None):
        AnagraficaScuole.objects.all().delete()
        permission_classes = [AllowAny]
        return Response(status=status.HTTP_200_OK)
