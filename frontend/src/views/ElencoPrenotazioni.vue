<template lang="html">
  <div class="container text-left">
      <h4 class="d-none d-print-block">Padova {{ dataAttuale}} </h4>
<!--    SELEZIONA LA DATA PRENOTAZIONE CON SELECT    -->
<div class ='d-print-none'>
 <font face="Times New Roman" size="3" color="#000000">
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
         <option value="EF" selected>Effettuata</option>
    </select>
    </font>
</div>

    <!--        -->
    <h3 id="dataPrenotazione" >Elenco Prenotazioni </h3>

    <!--    ELENCO COMPLETO PRENOTAZIONI    -->
    <!--    INTESTAZIONE DELLE COLONNE    -->
     <div class="row border-top border-secondary mb-2">
            <div class="col-md-8 "></div>
              <div class="col-md-3 ml-4 text-right">Mail Inviate</div>
     </div>
     <div class="row border-bottom border-secondary mb-2">
        <div class="col-md-2 ">Data</div>
        <div class="col-md-1 ">Status</div>
        <div class="col-md-1 ">Visita</div>
        <div class="col-md-2">Utente/Scuola</div>
        <div class="col-md-1 ">Accomp.</div>
        <div class="col-md-1 ">Alunni</div>
         <div class="col-md-3 ">Argomenti Preferiti</div>
        <div class="col-md-1 text-right">I.    C.   P.</div>
     </div>

<!--      Prenotazione -->
<font face="Times New Roman" size="1" color="#000000">
    <div  v-for="(prenotazione,index) in prenotazioni_filtered"   :key="index">
        <div class="row border-bottom">
            <div class="col-md-2 "
               v-text="prenotazione.data_prenotazione +  getTimehhmm(prenotazione.ora_prenotazione,prenotazione.scuola)  ">
             </div>
            <div class="col-md-1 " v-text="prenotazione.status"> </div>
            <div class="col-md-1 " v-text="prenotazione.tipoVisita"> </div>

                <!--   LINK ALla PRENOTAZIONE --> 
          <div  class="prenotazione-editor-link col-md-2" >
            <router-link
                v-if="prenotazione.nome_scuola "
                :to="{ name: 'prenotazione-editor', params: { pk: prenotazione.id, prenotazione:prenotazione} }"
                title = "Modifica Prenotazione"
                >  {{ prenotazione.nome_scuola }}
            </router-link>

            <router-link
                v-if="!prenotazione.nome_scuola "
                :to="{ name: 'prenotazione-editor', params: { pk: prenotazione.id, prenotazione:prenotazione } }"
                class="prenotazione-editor-link"
                title = "Modifica Prenotazione"
                >   {{ prenotazione.user }}
            </router-link>
          </div>
            
            <div class="col-md-1 text-center" v-text="prenotazione.numero_accompagnatori"> </div>
            <div class="col-md-1 text-center" v-text="prenotazione.numero_totale_alunni"> </div>
            <div class="col-md-3 " v-text="prenotazione.argomentiPreferiti "> </div>
            <div class="col-md-1 text-right">
            <input title="Mail Informativa Inviata" type="checkbox" onclick="return false;"  v-model="prenotazione.mailInformativaInviata">
            <input  title="Mail Conferma Inviata" class = " ml-1" type="checkbox" onclick="return false;"  v-model="prenotazione.mailConfermaInviata">
            <input  title="Pagato" class = " ml-1" type="checkbox" onclick="return false;"  v-model="prenotazione.pagato">
      </div>
      <br>

      <!--    MOVIMENTI PRENOTAZIONE --> 
      <div  v-for="(movimentoPrenotazione,index) in movimentiPrenotazioni"   :key="index">
        <div class="container "  v-if="movimentoPrenotazione.prenotazione == prenotazione.id ">
            <div class="col-12">
                <span class="col-md-3"  >Orario:{{getDescrizioneOrarioTurno(movimentoPrenotazione.turno)}} </span>
                <span class="col-md-3" > Settore: {{getDescrizioneSettoreTurno(movimentoPrenotazione.turno)}} </span>
                <span class="col-md-3" > Classe: {{movimentoPrenotazione.classe}} </span>
                <span class="col-md-3"> Alunni: {{movimentoPrenotazione.numero_alunni}} </span>
              </div>
          </div>
      </div>
              
   </div>
    </div>
   
    </font>      <!--        FINE FONT -->
    <!--        Fine Elenco movimenti prenotazione -->

  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
import { FormatToLocalDateString } from "../common/methods.js";

export default {
  name: "ElencoPrenotazioni",



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
    currentUser:{},
   
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
      getTimehhmm(Time,Scuola) {
    
        if (Scuola) {
           return ""
        }
        if(Time != null) {
          var Timehhmm = " - " + Time.toString().substring(0,5)
          }
        else {
           Timehhmm = ""
            }
        return Timehhmm;
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
        // let endpoint = `/api/prenotazioni/`;
         apiService(endpoint).then(data => {
        this.prenotazioni.push(...data.results);
         });
    },

    getPrenotazioniFilteredByDataPrenotazione() {
        this.prenotazioni_filtered = [];
        if (this.data_prenotazione != null ) {
            let endpoint = `/api/prenotazioni/?search=${this.setDateTOYYYYMMDD(this.data_prenotazione)}`;
            //alert(endpoint)
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
            let endpoint = `/api/prenotazioni/?ordering=-data_prenotazione&search=${this.status}`;
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


          getDescrizioneSettoreTurno(varIdTurno) {
          var j,descrizioneSettoreTurno;
          for (j=0; j<this.turni.length; j++) {
             if (this.turni[j].id == varIdTurno) {
                  descrizioneSettoreTurno = this.turni[j].settore
              }
          }
          return (descrizioneSettoreTurno)
        },


    getDescrizioneOrarioTurno(varIdTurno) {
        var j,descrizioneOrarioTurno;
        for (j=0; j<this.turni.length; j++) {
          if (this.turni[j].id == varIdTurno) {
                descrizioneOrarioTurno = this.turni[j].orario_turno
            }
        }
        return (descrizioneOrarioTurno)
      },



    async getMovimentiPrenotazioni() {
      let endpoint = `/api/movimentiPrenotazioni/`;
      apiService(endpoint).then(data => {
        this.movimentiPrenotazioni.push(...data.results);
      });
    },

      getUserName() {
            this.currentUser = {};
             let endpoint = "/api/user/";
             apiService(endpoint)
               .then(data => {
                 this.currentUser.id = data.id;
                 this.currentUser.userName = data.username;
                 this.currentUser.isStaff = data.is_staff;
                 this.userName=data.username;
              })
         },

   


  },

  created() {
    this.getUserName();
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
