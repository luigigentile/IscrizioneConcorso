import locale
from rest_framework import serializers
from prenotazioni.models import TabellaTurni,TabellaSettori,TabellaRuoli
from prenotazioni.models import Prenotazione,MovimentiPrenotazione,AnagraficaScuole,AnagraficaVideo
#locale.setlocale(locale.LC_ALL, 'it_IT.UTF8')

locale.setlocale(locale.LC_ALL, '')

class MovimentiPrenotazioneSerializer(serializers.ModelSerializer):
#    created_at = serializers.SerializerMethodField(read_only=True)
#    numero_alunni_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MovimentiPrenotazione
        fields = ["id","prenotazione","created_at","turno",'classe','numero_alunni']
#        fields = '__all__'
#    def get_created_at(self, instance):
#        return instance.created_at.strftime('%d %B %Y')
#
#    def get_numero_alunni_count(self, instance):
#        return instance.prenotazione.count()

class PrenotazioneSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    data_prenotazione = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
#    created_at = serializers.SerializerMethodField(read_only=True)
#    data_prenotazione = serializers.SerializerMethodField(read_only=False)

    class Meta:
        model = Prenotazione
        fields = ['id','user','created_at','data_prenotazione','ora_prenotazione','scuola','pagato','status','nome_scuola','numero_accompagnatori','numero_totale_alunni','esigenze',
        'argomentiPreferiti','tipoVisita','mailInformativaInviata','mailConfermaInviata','labelStatus']
        
#        fields = '__all__'

    #def aaa(self, instance):
   
#        return instance.created_at.strftime('%d %B %Y')


class DataPrenotazioniSerializer(serializers.ModelSerializer):
    data_prenotazione = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])

#    data_prenotazione = serializers.SerializerMethodField(read_only=False)
    class Meta:
        model = Prenotazione
        fields = ['data_prenotazione']

class TurniSerializer(serializers.ModelSerializer):
    settore = serializers.StringRelatedField(read_only=True)
    #settore = serializers.StringRelatedField()
    data = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])

#    data = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = TabellaTurni
        fields = '__all__'

#    def get_data(self, instance):
#        return instance.data.strftime('%d %B %Y')
#
class ListaTurniSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabellaTurni
        fields = '__all__'

class DataTurniSerializer(serializers.ModelSerializer):
    data = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])

    class Meta:
        model = TabellaTurni
        fields = ['data']
#    def get_data(self, instance):
#        return instance.data.strftime('%d %B %Y')

class SettoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabellaSettori
        fields = '__all__'


class AnagraficaScuoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnagraficaScuole
        fields = '__all__'

class AnagraficaVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnagraficaVideo
        fields = ["id","titolo","descrizione","note",'collegamento','settore']
    #    fields = '__all__'

class TabellaRuoliSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabellaRuoli
        fields = '__all__'
