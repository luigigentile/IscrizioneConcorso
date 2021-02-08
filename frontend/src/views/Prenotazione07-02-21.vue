<template lang="html">
  <!-- DESCRIZIONE  PRENOTAZIONE EFFETTUATA -->
  <div class="container text-left" >
      <h4 class="d-none d-print-block">Padova {{ getLocalDate(dataAttuale)}} </h4>
    <div class="card  border-primary rounded ">
        <div class="card-header" >
            <p  ><strong>PRENOTAZIONE:</strong>
                <a href="#" title="Inserisci turni  prenotazione"> 
                    <span class ='d-print-none btn btn-sm btn-primary ml-3' @click="setDisplayInsertPrenotazione">Nuovo Turno
                        <svg width="13" height="13" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                          <path fill="#70bf2b" d="M1600 796v192q0 40-28 68t-68 28h-416v416q0 40-28 68t-68 28h-192q-40 0-68-28t-28-68v-416h-416q-40 0-68-28t-28-68v-192q0-40 28-68t68-28h416v-416q0-40 28-68t68-28h192q40 0 68 28t28 68v416h416q40 0 68 28t28 68z"/>
                        </svg>
                    </span>
                </a>
 <!--   stampante
                <span class ='d-print-none' @click="stampa" >  <img src="/static/apps_printer_15747.png" style = 'max-width:3%' ></span>
-->
              <br>Data Prenotazione {{ prenotazione.data_prenotazione }}
              <br>Prenotazione Effettuata da : <strong class="author-name">   {{ prenotazione.user }}</strong>
              <br>Numero Accompagnatori: {{ prenotazione.numero_accompagnatori}} <br>
               <span>Numero Totale Alunni: {{ prenotazione.numero_totale_alunni}}</span><br>
               <span>Esigenze: {{ prenotazione.esigenze}}</span>
           </p>
          </div>
    </div>
     <!-- FINE DESCRIZIONE  PRENOTAZIONE EFFETTUATA -->

    <!--    INTESTAZIONE DELLE COLONNE    -->
    <div class="container border-bottom border-secondary">
        <div class="row  rounded" >
          <div class="col-md-2 ml-4 mr-1  ">Data</div>
          <div class="col-md-2 ">Orario</div>
          <div class="col-md-3 ">Settore</div>
          <div class="col-md-2 ">Classe</div>
          <div class="col-md-2 text-right ">N.ro Alunni</div>
        </div>
    </div>

    <!--    Elenco movimenti prenotazione    -->
    <div class="container border-bottom" v-for="(turnoPrenotazione,index) in movimentiPrenotazione"   :key="index">
        <div class="row">
    <!--    icona delete     -->
        <router-link title="Elimina turno Prenotazione"
                :to="{ name: 'movimento-prenotazione-confirm-delete', params: {prenotazione: prenotazione,turnoPrenotazione: turnoPrenotazione,pk: turnoPrenotazione.id} }"
                ><span class ='d-print-none'>
                    <svg width="14" height="14" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                      <path fill="#dd4646" d="M1490 1322q0 40-28 68l-136 136q-28 28-68 28t-68-28l-294-294-294 294q-28 28-68 28t-68-28l-136-136q-28-28-28-68t28-68l294-294-294-294q-28-28-28-68t28-68l136-136q28-28 68-28t68 28l294 294 294-294q28-28 68-28t68 28l136 136q28 28 28 68t-28 68l-294 294 294 294q28 28 28 68z"/>
                  </svg>
                  </span>
          </router-link>
    <!--    icona modifica     -->
            <a class ='d-print-none' href="#" title="Modifica turno Prenotazione">
                <span @click="ModificaPrenotazione(turnoPrenotazione)">
                <svg width="13" height="13" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                  <path fill="#efb80b" d="M491 1536l91-91-235-235-91 91v107h128v128h107zm523-928q0-22-22-22-10 0-17 7l-542 542q-7 7-7 17 0 22 22 22 10 0 17-7l542-542q7-7 7-17zm-54-192l416 416-832 832h-416v-416zm683 96q0 53-37 90l-166 166-416-416 166-165q36-38 90-38 53 0 91 38l235 234q37 39 37 91z"/>
                </svg>
                </span>
            </a>

        <div class="col-md-2 " v-text="getDataTurno(turnoPrenotazione.turno)"> </div>
        <div class="col-md-2 " v-text="getDescrizioneOrarioTurno(turnoPrenotazione.turno)"> </div>
        <div class="col-md-3" v-text="getDescrizioneSettoreTurno(turnoPrenotazione.turno)"> </div>

        <div class="col-md-2 " v-text="turnoPrenotazione.classe"> </div>
        <div class="col-md-2 text-right" v-text="turnoPrenotazione.numero_alunni"> </div>
        </div>
    </div>
    <!--    Fine Elenco movimenti prenotazione    -->

    <!--    Inserisci/Modifica prenotazione    -->
    <!--    Form Input data    -->
        <br>
        <form class ="mt-2 " v-show="displayEditorPrenotazione" @submit.prevent="AddInsertPrenotazione">
            <div class="row">
              <div class="col-lg-4 ml-3 border-bottom border-secondary ">Turno</div>
              <div class="col-lg-2 border-bottom border-secondary ">Classe</div>
              <div class="col-lg-2 border-bottom border-secondary">Disponibilità</div>
              <div class="col-lg-1 border-bottom border-secondary text-right">Alunni</div>
             </div>
             <br>

          <div class="form-row">
        <!--    TURNO    -->
            <div class="col-4 ">
            <select id = "SelectTurno" class="form-control mb-1"
                v-model='turno'
                  @change="getSelectedUserTurno">
                    <option disabled >Data Prenotazione: {{ prenotazione.data_prenotazione }}</option>
                  <optgroup   label="Orario -  Settore   - Posti Disponibili">
                   <option 
                      v-for="turno in turniFiltrati"
                      :key="turno.id"
                      :value=turno.id
                    >   {{ turno.orario_turno }} - {{ turno.settore }} - {{ turno.numero_posti_disponibili - getNumeroAlunniPrenotatiPerTurno(turno.id) }}
                  </option>
                     </optgroup>
            </select>
        </div>

            <div class="col-2">
              <input type="text" id ="classe" class="form-control" placeholder="classe" v-model="classe">
            </div>
            <div class="col-2">
            <p class="form-control" id="postiPrenotati">  {{ postiDisponibili }}</p>
            </div>

            <div class="col-2">
              <input type="number" id="numeroAlunni"  @change="checkNumeroAlunni" class="form-control" placeholder="numero alunni" v-model.number="numeroAlunni">
            </div>
            <div class="col-2">
            <button  class="btn btn-outline-primary "  >{{labelPulsanteAggiungi}}</button>
                </div>
          </div>


        </form>
<!--    end Form Inputa data    -->

  </div>

</template>

<script>
import { apiService } from "../common/api.service.js";
import { FormatToLocalDateString } from "../common/methods.js";

export default {
  name: "Prenotazione",

  props: {
    pk: {
      type: Number,
      required: true
    },
    prenotazione: {
    type: Object,
    required:false
    },
  },

  data() {
    return {
      previousPrenotazione:{},
      movimentiPrenotazione: [],
      movimentiPrenotazioni: [],
      postiPrenotatiPerTurno: [],
      postiPrenotati : null,
      postiDisponibili : null,
      idMovimentoPrenotazione:null,
      idPrenotazione:null,
      turni: [],
      turniFiltrati: [],
      settori:[],
      displayEditorPrenotazione: null,
      displayInsertPrenotazione:true,
      displayUpdatePrenotazione: false,
      turno:null,
      classe:null,
      numeroAlunni:null,
      numeroAlunniPrevious: null,
      numeroPostiDisponibili: null,
      loadingPrenotazione: false,
      showForm: false,
      error: null,
      next: null,
      requestUser: null,
      requestUrl: null,
      dataAttuale:null,
      labelPulsanteAggiungi : 'Aggiungi'
    };
  },
  computed: {
    isOwner() {
      //            return this.question.author === this.requestUser;
      return false;
    },
    notFound() {
      return this.prenotazione["detail"];
    }
  },


  methods: {

    labelOptGroup() {
          return "data:" +  " - Turno - Settore"
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

      getDataTurno(varIdTurno) {
          var j,dataTurno;
          for (j=0; j<this.turni.length; j++) {
             if (this.turni[j].id == varIdTurno) {
                  dataTurno = this.turni[j].data
              }
          }
          return (dataTurno)
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


      getLocalDate(Data) {
        return FormatToLocalDateString(Data);
          },

    setPageTitle(title) {
      document.title = title;
    },

    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    },


    getSelectedUserTurno() {
        var idTurno
        idTurno = document.getElementById("SelectTurno").value
        this.postiPrenotati = this.postiPrenotatiPerTurno[idTurno];
        this.numeroAlunni = 0
//        this.postiDisponibili = this.turni[idTurno-1].numero_posti_disponibili - this.postiPrenotati
        this.postiDisponibili = this.getNumeroPostiDisponibili(idTurno)- this.postiPrenotati
        document.getElementById("classe").focus();
        return

    },

    checkNumeroAlunni() {
//      CONTROLLA SE IL NUMERO DI ALUNNI E' NEGATIVO
      if (this.numeroAlunni < 0) {
            alert("Attenzione !!!! il numero di alunni non puo' essere negativo")
            this.numeroAlunni = this.numeroAlunniPrevious
            document.getElementById("numeroAlunni").focus();
            return
        }
//      CONTROLLA SE C'E' DISPONIBILITA'
       if (this.numeroAlunni - this.numeroAlunniPrevious > this.postiDisponibili) {
            alert("Attenzione non ci sono abbastanza posti disponibili")
            document.getElementById("numeroAlunni").focus();
            return false
        }
        return true
    },

    setDisplayEditorPrenotazione() {
        this.displayEditorPrenotazione  = !this.displayEditorPrenotazione;
        },

    setDisplayInsertPrenotazione() {
            this.setDisplayEditorPrenotazione()
            this.clearDataPrenotazione()
            this.getMovimentiPrenotazioni()
            this.operation = "insert"
            this.labelPulsanteAggiungi = "Aggiungi"
            this.numeroAlunniPrevious = 0
            this.displayInsertPrenotazione = true
            this.displayUpdatePrenotazione = false
        },

    async getMovimentiPrenotazione() {
      let endpoint = `/api/prenotazione/${this.pk}/movimenti/`;
      this.idPrenotazione = this.pk
      this.movimentiPrenotazione = []
//      alert("Prenotazione modificata Correttamente");
      apiService(endpoint).then(data => {
        this.movimentiPrenotazione.push(...data.results);
      });
    },

    async getMovimentiPrenotazioni() {
      let endpoint = `/api/movimentiPrenotazioni/`;
      this.movimentiPrenotazioni = [];
      apiService(endpoint).then(data => {
        this.movimentiPrenotazioni.push(...data.results);
      });
    },


    getNumeroAlunniPrenotatiPerTurno(idturno) {
        var j
        var numeroTotaleAlunni
        numeroTotaleAlunni = 0
        this.postiPrenotatiPerTurno[idturno] = 0
        for (j=0; j<this.movimentiPrenotazioni.length; j++) {
           if (this.movimentiPrenotazioni[j].turno == idturno) {
                   numeroTotaleAlunni = numeroTotaleAlunni + this.movimentiPrenotazioni[j].numero_alunni
    //               alert("turno =" + idturno +" posti prenotati = " + this.postiPrenotatiPerTurno[idturno])
                   this.postiPrenotatiPerTurno[idturno] = numeroTotaleAlunni
           }
        }
        return this.postiPrenotatiPerTurno[idturno]

    },


//    getNumeroAlunniPrenotatiPerOrarioTurno(idturno) {
//        var j
//        var numeroTotaleAlunni
//        numeroTotaleAlunni = 0
//        alert(turni(idturno).orario_turno)
//    },


    getNumeroPostiDisponibili(idTurno) {
    var j
       for (j=0; j<this.turni.length; j++) {
           if (this.turni[j].id == idTurno) {
                return this.turni[j].numero_posti_disponibili
           }
        }
    return 0
    },

    getNumeroPostiDisponibiliNew(idturno) {
        var j
        var numeroPostiDisponibili
        numeroPostiDisponibili = 0
        for (j=0; j<this.turni.length; j++) {
           if (this.turni[j].turno == idturno) {
                   numeroPostiDisponibili = this.turni[j].numero_posti_disponibili
            }
        }
        return numeroPostiDisponibili
    },

    getTurni() {
          let endpoint = `/api/turni/`;
          apiService(endpoint).then(data => {
            this.turni.push(...data.results);
        });
    },

    getTurniFiltratiPerDataPrenotazione(dataPrenotazione) {
//         let endpoint = `/api/prenotazioni/${this.pk}/movimenti/`;
        let endpoint = `/api/turni/?search=${this.setDateTOYYYYMMDD(dataPrenotazione)}`;
        apiService(endpoint).then(data => {
          this.turniFiltrati.push(...data.results);
      });
    },

    getSettoreTurno(IdTurno) {
        return this.settori[IdTurno];
    },

    getSettori() {
          let endpoint = `/api/settori/`;
          apiService(endpoint).then(data => {
            this.settori.push(...data.results);
        });
    },
    clearDataPrenotazione() {
        this.turno = null,
        this.classe = null,
        this.numeroAlunni = null
    },
    AddInsertPrenotazione() {
               if (this.checkNumeroAlunni() == false) {
                    return
                }
               if (this.operation == 'insert') {
                let endpoint = `/api/prenotazioni/${this.pk}/movimento/`;
                apiService(endpoint, "POST", { prenotazione:this.pk,turno: this.turno,classe: this.classe,numero_alunni:this.numeroAlunni})
                alert("Turno di prenotazione aggiunto correttamente")
                this.getMovimentiPrenotazione()
                this.postiDisponibili = 0
                }

               if (this.operation == 'update') {
                    let endpoint = `/api/movimentiPrenotazioni/${this.idMovimentoPrenotazione}/`;
                    apiService(endpoint, "PUT", { prenotazione:this.pk,turno: this.turno,classe: this.classe,numero_alunni:this.numeroAlunni})
                    alert("Turno di prenotazione modificato correttamente");
                    this.getMovimentiPrenotazione()
                }

                this.$forceUpdate()
                    this.$router.push({
                    name: "Home"
                })

                this.$router.push({
                    name: "prenotazione",
                    params: { pk: this.pk, prenotazione: this.previousPrenotazione }
                })
                this.$forceUpdate()
                this.clearDataPrenotazione()
                this.displayEditorPrenotazione = false
            },


        ModificaPrenotazione(prenotazione) {
            this.setDisplayEditorPrenotazione()
                this.operation = "update";
                this.labelPulsanteAggiungi = "Modifica"
                this.clearDataPrenotazione()
                this.getMovimentiPrenotazioni()
                this.idMovimentoPrenotazione = prenotazione.id;
                this.turno = prenotazione.turno;
                this.classe = prenotazione.classe;
                this.numeroAlunni = prenotazione.numero_alunni;
                this.numeroAlunniPrevious = this.numeroAlunni
                this.postiDisponibili = this.getNumeroPostiDisponibili(this.turno) - this.postiPrenotatiPerTurno[this.turno] ;
                this.displayInsertPrenotazione = false
                this.displayUpdatePrenotazione = true
                },


  },
  async created() {
    this.getMovimentiPrenotazione();
    this.getMovimentiPrenotazioni();
    this.getTurni();
    this.getSettori();
    this.previousPrenotazione = this.prenotazione;
    this.getTurniFiltratiPerDataPrenotazione(this.prenotazione.data_prenotazione)
    document.title = "Elenco Prenotazioni";
    this.dataAttuale = new Date();
},


};
</script>

<style lang="css" scoped></style>
