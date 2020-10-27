<template lang="html">
  <div class="container">
      <h4 class="d-none d-print-block">Padova {{ dataAttuale}} </h4>
<!--    SELEZIONA LA DATA PRENOTAZIONE CON SELECT    -->
<div class ='d-print-none'>
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
</div>

    <!--        -->
            <h3 id="dataPrenotazione" >Elenco Prenotazioni</h3>

    <!--    ELENCO COMPLETO PRENOTAZIONI    -->
    <!--    INTESTAZIONE DELLE COLONNE    -->
        <div class="row border-bottom border-secondary mb-2">
        <div class="col-md-2 ">Data</div>
        <div class="col-md-1 ">Status</div>
        <div class="col-md-4">Nome Scuola/Utente</div>
        <div class="col-md-1 ">Accomp.</div>
        <div class="col-md-1 ">Alunni</div>
        <div class="col-md-3 ">Esigenze</div>
        </div>

<!--      Elenco movimenti prenotazione -->
<font face="Times New Roman" size="2" color="#000000">
    <div  v-for="(prenotazione,index) in prenotazioni_filtered"   :key="index">
        <div class="row border-bottom">
            <div class="col-md-2 " v-text="prenotazione.data_prenotazione"> </div>
            <div class="col-md-1 " v-text="prenotazione.status"> </div>
<!--   LINK AL DETTAGLIO PRENOTAZIONE
            <router-link  v-if="prenotazione.scuola || staff " title="Visualizza dettagli Prenotazione"
              :to="{ name: 'prenotazione', params: {pk: prenotazione.id , prenotazione:prenotazione} }"
              class="prenotazione-link col-md-4"
            >Data Prenotazione {{ prenotazione.nome_scuola }}
            </router-link>
-->

<!--   LINK ALla PRENOTAZIONE -->
            <router-link
                v-if="prenotazione.scuola"
                :to="{ name: 'prenotazione-editor', params: { pk: prenotazione.id, prenotazione:prenotazione} }"
                class="prenotazione-editor-link col-md-4"
                title = "Modifica Prenotazione"
                >  {{ prenotazione.nome_scuola }}
            </router-link>

            <router-link
                v-else
                :to="{ name: 'prenotazione-editor', params: { pk: prenotazione.id, } }"
                class="prenotazione-editor-link col-md-4"
                title = "Modifica Prenotazione"
                >   {{ prenotazione.user }}
            </router-link>


            <div class="col-md-1 text-center" v-text="prenotazione.numero_accompagnatori"> </div>
            <div class="col-md-1 text-center" v-text="prenotazione.numero_totale_alunni"> </div>
            <div class="col-md-3 " v-text="prenotazione.esigenze"> </div>
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
    turni:[],
    movimentiPrenotazioni: [],
    postiPrenotati : null,
    next: null,
    loadingPrenotazioni: false,
    dataAttuale:null,
  };
  },


  methods: {
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
            let endpoint = `/api/prenotazioni/?search=${this.setDateTOYYYYMMDD(this.data_prenotazione)}`;
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
    this.dataAttuale = new Date();
  }
};
</script>
