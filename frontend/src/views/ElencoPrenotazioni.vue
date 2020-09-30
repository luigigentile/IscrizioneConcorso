<template lang="html">
  <div class="container">

<!--    SELEZIONA LA DATA PRENOTAZIONE CON SELECT    -->
    <label for="dataPrenotazione" class='mr-1'>Data Prenotazione </label>
            <select  id="dataPrenotazione"
            class="col-3 mr-2"
             placeholder="data prenotazione"
             v-on:change="getPrenotazioniFilteredByDataPrenotazione"
             v-model="data_prenotazione">
             <option value="">All.....</option>
              <option
               v-for="prenotazione in distinct_data_prenotazione"
               :key="prenotazione.id"
               >{{ prenotazione.data_prenotazione }}
           </option>
            </select>
<!--    SELEZIONA LO STATUS  CON SELECT    -->
    <label for="idstatus" class='mr-1'>Status</label>
    <select  id="idstatus"
     class="col-3"
     placeholder="status"
     v-on:change="getPrenotazioniFilteredByStatus"
     v-model="status">
         <option value="">All.....</option>
         <option value="DC">Da Confermare</option>
         <option value="CO" selected>Confermato</option>
    </select>
    <!--        -->
            <h2 id="dataPrenotazione" >Elenco Prenotazioni</h2>

    <!--    ELENCO COMPLETO PRENOTAZIONI    -->
    <!--    INTESTAZIONE DELLE COLONNE    -->
        <div class="row">
        <div class="col-lg-2 border-bottom border-secondary ">Data</div>
        <div class="col-lg-1 border-bottom border-secondary ">Status</div>
        <div class="col-lg-2 border-bottom border-secondary">Nome Scuola</div>
        <div class="col-lg-2 border-bottom border-secondary">Numero Accompagnatori</div>
        <div class="col-lg-1 border-bottom border-secondary ">Numero Alunni</div>
        <div class="col-lg-4 border-bottom border-secondary ">Esigenze</div>
        </div>

<!--      Elenco movimenti prenotazione -->
<font face="Times New Roman" size="2" color="#000000">
    <div  v-for="(prenotazione,index) in prenotazioni_filtered"   :key="index">
        <div class="row">
            <div class="col-lg-2 border-bottom " v-text="getLocalDate(prenotazione.data_prenotazione)"> </div>
            <div class="col-lg-1 border-bottom" v-text="prenotazione.status"> </div>
            <div class="col-lg-2 border-bottom" v-text="prenotazione.nome_scuola"> </div>
            <div class="col-lg-2 border-bottom" v-text="prenotazione.numero_accompagnatori"> </div>
            <div class="col-lg-1 border-bottom " v-text="prenotazione.numero_totale_alunni"> </div>
            <div  class="col-lg-4 border-bottom " v-text="prenotazione.esigenze"> </div>
        </div>
    </div>
    </font>
    <!--        Fine Elenco movimenti prenotazione -->


  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
import { FormatToLocalDateString } from "../common/methods.js";

export default {
  name: "RiepilogoPrenotazioni",



  data() {
    return {
        space : "    ",
      prenotazioni: [],
      prenotazioni_filtered: [],
      distinct_data_prenotazione:[],
      status:null,
      data_prenotazione:null,
      filtro:null,
      turni:[],
      movimentiPrenotazioni: [],
      postiPrenotati : null,
      next: null,
      loadingPrenotazioni: false,
  };
  },




  methods: {

      getLocalDate(Data) {
    //    return new Date(DataPrenotazione).toLocaleDateString();
        return FormatToLocalDateString(Data);
          },

      getToISOString(DataPrenotazione) {
    //    return new Date(DataPrenotazione).toLocaleDateString();
        return new Date(DataPrenotazione).toISOString();
          },



    getPrenotazioni() {
      let endpoint = `/api/prenotazioni/?ordering=data_prenotazione`;
     apiService(endpoint).then(data => {
        this.prenotazioni.push(...data.results);
         });
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

    getPrenotazioniFilteredByStatus() {
        this.prenotazioni_filtered = [];

        if (this.status != null ) {
            this.filtro = this.status
            let endpoint = `/api/prenotazioni/?ordering=data_prenotazione&search=${this.status}`;
            apiService(endpoint).then(data => {
            this.prenotazioni_filtered.push(...data.results);
             });
         } else {
             this.prenotazioni_filtered = this.prenotazioni;
         }
    },

    getDistinctDataPrenotazione() {
          let endpoint = `/api/distinctdataprenotazione/`;
          apiService(endpoint).then(data => {
            this.distinct_data_prenotazione.push(...data.results);
        });
    },

    getTurni() {
          let endpoint = `/api/turni/?ordering=data`;
          apiService(endpoint).then(data => {
            this.turni.push(...data.results);
        });
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
    this.getPrenotazioniFilteredByDataPrenotazione()
    this.getTurni();
    this.getMovimentiPrenotazioni();
    this.getDistinctDataPrenotazione();


    //        document.getElementById('SelectUser').selectedIndex  = "1"
    document.title = "Elenco Prenotazioni";
  }
};
</script>
