<template lang="html">
  <div class="container">
  <!--    DATA PRENOTAZIONE CON SELECT    -->
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
  <!--        -->
    <h2>Riepilogo Prenotazioni</h2>

    <!--    RIEPILOGO TURNI CON PRENOTAZIONI    -->
    <!--    INTESTAZIONE DELLE COLONNE    -->
        <div class="row">
          <div class="col-lg-2 border-bottom border-secondary ">Data</div>
          <div class="col-lg-2 border-bottom border-secondary ">Orario</div>
          <div class="col-lg-2 border-bottom border-secondary">Settore</div>
          <div class="col-lg-1 border-bottom border-secondary text-right">Max</div>
          <div class="col-lg-2 border-bottom border-secondary text-right">Prenotati</div>
         <div class="col-lg-2 border-bottom border-secondary text-right">Disponibili</div>
        </div>

    <!--    Elenco movimenti prenotazione    -->
    <div class="container table-striped" v-for="(turno,index) in turni_filtrati"   :key="index">
        <div class="row">
            <div class="col-lg-2 border-bottom" v-text="turno.data"> </div>
            <div class="col-lg-2 border-bottom" v-text="turno.orario_turno"> </div>
            <div class="col-lg-2 border-bottom" v-text="turno.settore"> </div>
            <div class="col-lg-1 border-bottom text-right" v-text="turno.numero_posti_disponibili"> </div>
            <div class="col-lg-2 border-bottom text-right"> {{ getNumeroAlunniPrenotatiPerTurno(turno.id) }} </div>
            <div class="col-lg-2 border-bottom text-right" v-text="turno.numero_posti_disponibili-postiPrenotati"> </div>

        </div>
    </div>
        <!--    Fine Elenco movimenti prenotazione    -->


  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "RiepilogoPrenotazioni",

  data() {
    return {
      prenotazioni: [],
      turni:[],
      turni_filtrati:[],
      distinct_data_turni:[],
      data_turno:null,
      movimentiPrenotazioni: [],
      postiPrenotati : null,
      next: null,
      loadingPrenotazioni: false,
  };
  },

  methods: {
    getNumeroAlunniPrenotatiPerTurno(idturno) {
        var j
        var numeroTotaleAlunni
        this.postiPrenotati = 0
        numeroTotaleAlunni = 0
//        alert("idTurno= " + idturno)
       for (j=0; j<this.movimentiPrenotazioni.length; j++) {
            if (this.movimentiPrenotazioni[j].turno == idturno) {
                   numeroTotaleAlunni = numeroTotaleAlunni + this.movimentiPrenotazioni[j].numero_alunni
           }
        }
        this.postiPrenotati = numeroTotaleAlunni
        return numeroTotaleAlunni

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
        });
    },

    getDistinctDataTurni() {
          let endpoint = `/api/distinctdataturni/`;
          apiService(endpoint).then(data => {
            this.distinct_data_turni.push(...data.results);
        });
    },

    getTurniFiltratiPerData() {
    this.turni_filtrati = [];
    if (this.data_turno != null  && this.data_turno != "" ) {
            let endpoint = `/api/turni/?search=${this.data_turno}`;
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


    //        document.getElementById('SelectUser').selectedIndex  = "1"
    document.title = "Riepilogo Prenotazioni";
  }
};
</script>
