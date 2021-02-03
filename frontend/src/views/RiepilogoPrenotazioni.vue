<template lang="html">
  <div class="container text-left">

<h4 class="d-none d-print-block">Padova {{ getLocalDate(dataAttuale)}}</h4>

  <!--    DATA PRENOTAZIONE CON SELECT    -->
    <div class="d-print-none">
          <label for="dataTurno" class="col-3" >Data Prenotazione</label>
          <select  id="dataTurno"
           class="col-2" placeholder="data prenotazione"
           v-on:change="getTurniFiltratiPerData"
           v-model="data_turno">
            <option value="">All.....</option>
            <option
             v-for="turno in distinct_data_turni"
             :key="turno.id"
             >{{ turno.data }}
         </option>
          </select>
    </div>
  <!--   FINE DATA PRENOTAZIONE CON SELECT     -->

    <h3>Riepilogo Prenotazioni</h3>
    <!--    RIEPILOGO TURNI CON PRENOTAZIONI    -->
    <!--    INTESTAZIONE DELLE COLONNE    -->
        <div class="row border-bottom border-secondary mb-1">
          <div class="col-md-2 ">Data</div>
          <div class="col-md-2 ">Orario</div>
          <div class="col-md-2 ">Settore</div>
          <div class="col-md-2 text-right">Max</div>
          <div class="col-md-2 text-right">Prenotati</div>
          <div class="col-md-2 text-right">Disponibili</div>
        </div>

    <!--    Elenco movimenti prenotazione    -->
    <font face="Times New Roman" size="2" color="#000000">
    <div class="container border-bottom" v-for="(turno) in turni_filtrati"   :key="turno.id">
        <div class="row">
            <div class="col-md-2 " v-text="turno.data"> </div>
            <div class="col-md-2 " v-text="turno.orario_turno"> </div>
            <div class="col-md-2 " v-text="turno.settore"> </div>
            <div class="col-md-2  text-right" v-text="turno.numero_posti_disponibili"> </div>
            <div class="col-md-2  text-right" v-text="numeriAlunniPrenotatiPerTurno[turno.id]"> </div>
            <div class="col-md-2 border-bottom text-right" v-text="turno.numero_posti_disponibili-numeriAlunniPrenotatiPerTurno[turno.id]"> </div>
        </div>
    </div>
    </font>
        <!--    Fine Elenco movimenti prenotazione    -->


  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
import { FormatToLocalDateString } from "../common/methods.js";

export default {
  name: "RiepilogoPrenotazioni",

  data() {
    return {
      prenotazioni: [],
      turni:[],
      turni_filtrati:[],
      numeriAlunniPrenotatiPerTurno:[],
      distinct_data_turni:[],
      data_turno:null,
      movimentiPrenotazioni: [],
      postiPrenotati : null,
      next: null,
      loadingPrenotazioni: false,
      numeroTurni:null,
      dataAttuale:null,
  };
  },

  methods: {
     getLocalDate(Data) {
        return FormatToLocalDateString(Data);
          },

    getNumeroAlunniPrenotatiPerTurno(idturno) {
        var j
        var numeroTotaleAlunni
        this.postiPrenotati = 0
        numeroTotaleAlunni = 0
//        alert("idTurno= " )
       for (j=0; j<this.movimentiPrenotazioni.length; j++) {
            if (this.movimentiPrenotazioni[j].turno == idturno) {
                alert(this.movimentiPrenotazioni[j].turno)
                   numeroTotaleAlunni = numeroTotaleAlunni + this.movimentiPrenotazioni[j].numero_alunni
           }
        }
        this.postiPrenotati = numeroTotaleAlunni
        return numeroTotaleAlunni

    },

    getNumeroAlunniPrenotatiPerTurnoNew(idturno) {
        var j
        var numeroTotaleAlunni
        this.postiPrenotati = 0
        numeroTotaleAlunni = 0
//        alert("sono in geto= " + idturno)
       for (j=0; j<this.movimentiPrenotazioni.length; j++) {
            if (this.movimentiPrenotazioni[j].turno == idturno) {
//                    alert(this.movimentiPrenotazioni[j].turno)
                   numeroTotaleAlunni = numeroTotaleAlunni + this.movimentiPrenotazioni[j].numero_alunni
           }
        }
        this.postiPrenotati = numeroTotaleAlunni
        return numeroTotaleAlunni

    },

    SetNumeroAlunniPrenotatiPerTurno() {
        this.numeriAlunniPrenotatiPerTurno = []
        var i,j,idturno

//        alert("idTurno= " + idturno)
//        alert("this.movimentiPrenotazioni.length" + this.movimentiPrenotazioni.length)
        for (i=0; i<this.turni.length ;i++) {
            idturno =this.turni[i].id
            this.numeriAlunniPrenotatiPerTurno[idturno] = 0
            for (j=0; j<this.movimentiPrenotazioni.length; j++) {
//                    alert(this.movimentiPrenotazioni[j].turno)
//                    alert(this.turni[i].id)
                 if (this.movimentiPrenotazioni[j].turno == idturno) {
                     this.numeriAlunniPrenotatiPerTurno[idturno] = this.numeriAlunniPrenotatiPerTurno[idturno] + this.movimentiPrenotazioni[j].numero_alunni
                 }
             }

           }
        //        this.postiPrenotati = numeroTotaleAlunni
        return 0

    },

    getPrenotazioni() {
      let endpoint = `/api/prenotazioni/`;
      apiService(endpoint).then(data => {
        this.prenotazioni.push(...data.results);
         });
    },

    getTurni() {
          let endpoint = `/api/turni/?ordering=data`;
          apiService(endpoint).then(data => {
            this.turni.push(...data.results);
            this.numeroTurni =  this.turni.length
        });
    },

    getDistinctDataTurni() {
          let endpoint = `/api/distinctdataturni/`;
          apiService(endpoint).then(data => {
            this.distinct_data_turni.push(...data.results);
        });
    },

    setDateTOYYYYMMDD(varData) {
        if (varData == null) {
                return varData
            }
        if (varData.length == 0) {
                return varData
            }
        var anno,mese,giorno;
        anno = varData.substring(6,10);
        mese = varData.substring(3,5);
        giorno = varData.substring(0,2);
        return anno+"-"+mese+"-"+giorno
    },

    getTurniFiltratiPerData() {
    this.turni_filtrati = [];
    if (this.data_turno != null  && this.data_turno != "" ) {
            let endpoint = `/api/turni/?search=${this.setDateTOYYYYMMDD(this.data_turno)}`;
            apiService(endpoint).then(data => {
              this.turni_filtrati.push(...data.results);
             });
         } else {
             this.turni_filtrati = this.turni;
         }
    },



    getPrenotazioniFilteredByDataPrenotazione() {
        this.prenotazioni_filtered = [];

        if (this.data_prenotazione != null ) {
             this.filtro = this.data_prenotazione
            let endpoint = `/api/prenotazioni/?search=${this.data_prenotazione}`;
            apiService(endpoint).then(data => {
            this.prenotazioni_filtered.push(...data.results);
             });
         } else {
             this.prenotazioni_filtered = this.prenotazioni;
         }

    },

    async getMovimentiPrenotazioni() {
      let endpoint = `/api/movimentiPrenotazioni/`;
      apiService(endpoint).then(data => {
        this.movimentiPrenotazioni.push(...data.results);
      });
    },


  },

  created() {
    this.getPrenotazioni();
    this.getTurni();
    this.getMovimentiPrenotazioni();
    this.getDistinctDataTurni();
    this.getTurniFiltratiPerData();
    this.dataAttuale = new Date();



    //        document.getElementById('SelectUser').selectedIndex  = "1"
    document.title = "Riepilogo Prenotazioni";
},
    ready() {
        alert("ready")
    },

    beforeUpdate() {
        if (this.numeroTurni != null) {
            this.SetNumeroAlunniPrenotatiPerTurno();
//        alert("numero Turni" + this.numeroTurni)
}
    },



//    updated() {
//        alert("updated")
//        alert("numero Turni" + this.numeroTurni)
//    },

//    mounted() {
//            this.SetNumeroAlunniPrenotatiPerTurno();
//            alert(this.numeroTurni)
//        alert("mounted")
//    },

    destroyed() {

//        alert("destroyed")
    },



};
</script>
