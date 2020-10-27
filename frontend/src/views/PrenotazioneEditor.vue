<template lang="html">
    <div class="container">
<!--    Pulsante Dettaglio Prenotazione di Conferma -->
        <div class="container " >
            <div class="row  rounded" >
                <div class="col-md-8  ">
                      <h1 >{{title}} </h1>
                </div>
<!--    Pulsante Dettaglio Prenotazione di Conferma -->
                <div class="col-md-3 ml-3" v-if="previousscuola">
                     <span class="btn btn-outline-success  mt-3 btn-sm">
                     <router-link   title="Visualizza dettagli Prenotazione"
                       :to="{ name: 'prenotazione', params: {pk: prenotazione.id , prenotazione:prenotazione} }"
                       class="prenotazione-link"
                       >Dettaglio Prenotazioni
                       </router-link>
                      </span>
                 </div>

            </div>
        </div>

        <form @submit.prevent="onSubmit" >

        <div class = "border-bottom border-secondary pb-1" v-if="userIsStaff && pk">
    <!--    checkbox  pagato -->
            <input class="ml-3" type="checkbox" id="pagato"  v-model="pagato">
            <label class="ml-1 mr-4" for="pagato"> Pagato </label>
    <!--    STATUS   -->
            <label class="ml-1" for="id_status">Status:</label>
            <select class="ml-1" name="status" id="id_status" v-model="status">
                <option value="DC">Da Confermare</option>
                <option value="CO" selected>Confermato</option>
            </select>

    <!--    Pulsante Invia mail di Conferma -->
        <a class="btn btn-outline-success ml-4 btn-sm" v-if="prenotazioneIsConfermata()" @click="inviaMailConferma"
            >invia Mail Conferma
        </a>
        </div>


        <br>
        <!--    Pulsante Modifica Data Prenotazione
        <a class="btn btn-outline-success ml-4"  @click="modificaDataPrenotazione" >passa a.. </a>
        -->
<!--    checkbox  Scuola    -->
        <input class="ml-3" @change="updateScuola" type="checkbox" id="scuola"  v-model="scuola">
        <label class="ml-1" for="scuola"> scuola/gruppo </label><br>

<!--    DATA PRENOTAZIONE CON SELECT    -->
        <label for="dataPrenotazione" class="col-3" >Data Prenotazione</label>
        <select  id="dataPrenotazione"
            @change="changeDataPrenotazione"
            class="col-9" placeholder="data prenotazione"
            v-model="data_prenotazione">
            <option
               v-for="turno in distinct_data_turni"
               :key="turno.id"
               >{{ turno.data }}
             </option>
        </select>
        <br>

        <div v-if="scuola">
<!--    Nome Scuola con casella di testo e Select  -->
            <label for="nomescuola" class="col-3" >Nome Scuola/Gruppo</label>
            <input type="text" class="col-4" placeholder="nome scuola" v-model="nome_scuola" id="nomescuola" autofocus>
<!--    SELEZIONA LA SCUOLA CON SELECT    -->
            <select  id="nomescuola"
                class="col-4 ml-3"
                placeholder="nome scuola"
                v-model="nome_scuola">
                <option value=""></option>
                <option
                       v-for="scuola in scuole"
                       :key="scuola.codice_ministeriale"
                       >{{ scuola.sigla  }} - {{ scuola.nome_scuola }} - {{ scuola.comune }}
                </option>
            </select>
        </div>

                <!--    Data Prenotazione
                <label for="dataPrenotazione" class="col-3" >Data Prenotazione</label>
                <input id="dataPrenotazione" type="date"  class="col-9" placeholder="data prenotazione"
                    v-model="data_prenotazione">
                -->
                <!--    Numero accompagnatori    -->
                <label for="numeroAccompagnatori" class="col-3" >{{label_numero_accompagnatori}} </label>
                <input @change="changeNumeroAccompagnatori" id="numeroAccompagnatori" type="number"  class="col-9" placeholder="numero_accompagnatori"
                v-model.number="numero_accompagnatori">
                <!--    Numero Totale Alunni    -->
                    <div v-if="scuola">
                    <label for="numeroTotaleAlunni" class="col-3" >Numero Totale Alunni</label>
                    <input @change="changeNumeroTotaleAlunni" id="numeroTotaleAlunni" type="number"  class="col-9" placeholder="numero_totale_alunni"
                    v-model.number="numero_totale_alunni">
                    </div>

                <!--    esigenze    -->
                    <label for="esigenze" class="col-3" >Esigenze</label>
                    <input type="text" class="col-9" placeholder="esigenze" v-model="esigenze" id="esigenze" autofocus>

                    <br>
                    <br>
                    <button
                    class = 'btn btn-success'
                    type="submit"
                    > {{title}}
                    </button>

                    <button
                    @click="tornaIndietro"
                    class="btn  btn-primary ml-3">
                    No, torna indietro
                    </button>

                </form>
                <p class = 'muted error mt-2'> {{ error }}</p>
                <p class='muted error mt-2'></p>
    </div>

</template>

<script>



import { apiService } from "../common/api.service";
import { FormatToLocalDateString } from "../common/methods.js";

export default {
    name: "PrenotazioneEditor",
    props: {
        pk: {
            type: Number,
            required:false
        },
        prenotazione: {
            type: Object,
            required:false
        },
        previousData_Prenotazione: {
            type: String,
            required:false
            },
        previousscuola: {
            type: Boolean,
            required:false
            },
        previouspagato: {
            type: Boolean,
            required:false
            },
        previousNome_Scuola: {
            type: String,
            required:false
            },
        previousStatus: {
            type: String,
            required:false
            },
        previousEsigenze: {
            type: String,
            required:false
            },
        previousNumero_Totale_Alunni: {
            type: Number,
            required:false
        },
        previousNumero_Accompagnatori: {
            type: Number,
            required:false
        },
        from_Name: {
            type: String,
            required:false
        },

    },

    data() {
        return {
            title: null,
            lastPrenotazione:[],
            submitText:"Aggiungi Prenotazione",
            id:this.previousId || null,
            data_prenotazione:this.previousData_Prenotazione || null,
            scuole: [],
            scuola:this.previousscuola || false,
            pagato:this.previouspagato || false,
            nome_scuola:this.previousNome_Scuola || null,
            status:this.previousStatus || null,
            numero_accompagnatori: this.previousNumero_Accompagnatori  || 1,
            numero_totale_alunni: this.previousNumero_Totale_Alunni  || 0,
            esigenze: this.previousEsigenze  || null,
            error: null,
            requestUserName : null,
            userIsStaff:false,
            turni: [],
            distinct_data_turni:[],
            label_numero_accompagnatori:null,
            tipoOperazione : null,
        }
    },

    async beforeRouteEnter(to,from,next) {
        to.params.from_Name = from.name
        if(to.params.pk !== undefined) {
            let endpoint = `/api/prenotazioni/${to.params.pk}/`;
            await apiService(endpoint)
                    .then(data => {
                        to.params.previousData_Prenotazione = data.data_prenotazione;
                        to.params.previousscuola = data.scuola;
                        to.params.previouspagato = data.pagato;
                        to.params.previousNome_Scuola = data.nome_scuola;
                        to.params.previousStatus = data.status;
                        to.params.previousNumero_Accompagnatori = data.numero_accompagnatori;
                        to.params.previousNumero_Totale_Alunni = data.numero_totale_alunni;
                        to.params.previousEsigenze = data.esigenze;
                    })
                    .catch(error => console.log(error))
            }
        return next();
    },

    methods : {
            setDateTOYYYYMMDD(varData) {
            var anno,mese,giorno;
            anno = varData.substring(6,10);
            mese = varData.substring(3,5);
            giorno = varData.substring(0,2);
            return anno+"-"+mese+"-"+giorno
        },

        changeNumeroAccompagnatori() {
            if (this.numero_accompagnatori <= 0) {
                var messaggio
                messaggio = "Attenzione!!! il  numero " + this.label_numero_accompagnatori + " deve essere positivo"
                alert(messaggio)
                this.numero_accompagnatori = this.previousNumero_Accompagnatori
                document.getElementById("numeroAccompagnatori").focus();
                }
            },

            changeNumeroTotaleAlunni() {
                if (this.numero_totale_alunni < 0) {
                    var messaggio
                    messaggio = "Attenzione!!! il  numero di alunni deve essere positivo"
                    alert(messaggio)
                    this.numero_totale_alunni = this.previousNumero_Totale_Alunni
                    document.getElementById("numeroTotaleAlunni").focus();
                    }
                },

        changeDataPrenotazione() {
            if (this.scuola && this.tipoOperazione =="update") {
                var messaggio
                messaggio = "Gentile utente, le ricordiamo che se viene modificata la data di . \n"
                messaggio = messaggio + "prenotazione dovrà impostare nuovamente i turni di prenotazione perchè il sistema \n"
                messaggio = messaggio + "dovrà controllare la disponibilità di posti. \n"
                alert(messaggio)
                }
            },

            inviaMailConferma() {
            var reference
//          SALVA LA PRENOTAZIONE
            this.SetStatusField();
            let endpoint = `/api/prenotazioni/${this.pk}/`;
            alert(apiService(endpoint, "PUT", {data_prenotazione: this.data_prenotazione,
                                        scuola:this.scuola,
                                        pagato:this.pagato,
                                        nome_scuola:this.nome_scuola,
                                        status:this.status,
                                        numero_accompagnatori: this.numero_accompagnatori,
                                        numero_totale_alunni:this.numero_totale_alunni,
                                        esigenze:this.esigenze}))


            alert("La prenotazione è stata modificata correttamente \ned è stata inviata una mail di conferma all'utente: " + this.requestUserName)
            reference = "/mail-conferma-prenotazione/" + this.pk +"/"
            location.href = reference;
          },


            prenotazioneIsConfermata() {
            if(this.status=='CO') {
              return true
            }
            else {
              return false
            }
        },

        setRequestUserName() {
          this.requestUserName = window.localStorage.getItem("username");
          if (window.localStorage.getItem("isStaff") == "true") {
              this.userIsStaff = true;
          }
        },

        updateScuola() {
            if (this.scuola == true) {
                this.label_numero_accompagnatori = "Numero Accompagnatori"
            } else {
                this.label_numero_accompagnatori = "Numero Persone"
            }
        },

        getLocalDate(Data) {
            return FormatToLocalDateString(Data);
        },
        getTurni() {
              let endpoint = `/api/turni/`;
              apiService(endpoint).then(data => {
                this.turni.push(...data.results);
            });
        },
        getScuole() {
              let endpoint = `/api/scuole/`;
              apiService(endpoint).then(data => {
                this.scuole.push(...data.results);
            });
        },
        getDistinctDataTurni() {
              let endpoint = `/api/distinctdataturni/`;
              apiService(endpoint).then(data => {
                this.distinct_data_turni.push(...data.results);
            });
        },
        getLastPrenotazione() {
          //          let endpoint = `/api/prenotazioni/${this.pk}/`;
          this.lastPrenotazione=[];
          let endpoint = "api/prenotazioni/?ordering=-id";
          apiService(endpoint).then(data => {
             this.lastPrenotazione[0] = data.results[0];
               this.$router.push({
                      name: "prenotazione",
                      params: {pk: this.lastPrenotazione[0].id , prenotazione:this.lastPrenotazione[0]}
                  })
            });
        },
        tornaIndietro() {
            this.$router.push({
                name: this.from_Name
            })
//        window.history.back()
         },

         vaiAMovimentiPrenotazione() {
            this.$router.push({
                 name: "prenotazione",
                 params: {pk: this.lastPrenotazione[0].id , prenotazione:this.lastPrenotazione[0]}
             })
           },


           modificaDataPrenotazione() {
               if (this.previousData_Prenotazione) {
                var newDate ='2021-03-09'
                   alert(newDate)
                   this.SetStatusField();
                   let endpoint = `/api/prenotazioni/${this.pk}/`;
                   alert(typeof(this.newDate));
                   apiService(endpoint, "PUT", {data_prenotazione: newDate,
                                               scuola:this.scuola,
                                               pagato:this.pagato,
                                               nome_scuola:this.nome_scuola,
                                               status:this.status,
                                               numero_accompagnatori: this.numero_accompagnatori,
                                               numero_totale_alunni:this.numero_totale_alunni,
                                               esigenze:this.esigenze})
                                            }
                      },


        onSubmit() {
            var messaggio,reference
            if (!this.previousData_Prenotazione) {
                let endpoint = `/api/prenotazioni/`;
                apiService(endpoint, "POST", {data_prenotazione: this.data_prenotazione,
                                                numero_accompagnatori: this.numero_accompagnatori,
                                                scuola:this.scuola,
                                                nome_scuola:this.nome_scuola,
                                                numero_totale_alunni:this.numero_totale_alunni,
                                                esigenze:this.esigenze})


                messaggio = "Gentile utente, \ngrazie di aver prenotato una visita alla mostra  Sperimentando.  \n"
                if (this.scuola) {
                    messaggio = messaggio + "Per completare la prenotazione, Le ricordo che bisogna inserire i turni e i settori da visitare.\n"
                    }
                messaggio = messaggio + "La preghiamo di attendere la nostra mail di conferma da parte di Sperimentando \n"
                messaggio = messaggio + "Distinti saluti,\nlo staff di Sperimentando"
                alert(messaggio)
//        SI POSIZIONE SULL'ULTIMA PRENOTAZIONE O TORNA ALLA PAGINA home
                if (this.scuola) {
                    this.getLastPrenotazione()
                }else {
                    this.tornaIndietro()
                }
//                this.vaiAMovimentiPrenotazione();
            }
            if (this.previousData_Prenotazione) {
                this.SetStatusField();
                let endpoint = `/api/prenotazioni/${this.pk}/`;
                apiService(endpoint, "PUT", {data_prenotazione: this.data_prenotazione,
                                            scuola:this.scuola,
                                            pagato:this.pagato,
                                            nome_scuola:this.nome_scuola,
                                            status:this.status,
                                            numero_accompagnatori: this.numero_accompagnatori,
                                            numero_totale_alunni:this.numero_totale_alunni,
                                            esigenze:this.esigenze})
                if(this.data_prenotazione != this.previousData_Prenotazione && this.scuola) {

                    messaggio = "Gentile utente, la sua prenotazione è stata modificata correttamente. \n"
                    messaggio = messaggio + "Attenzione avendo cambiato la data di prenotazione è necessario \n"
                    messaggio = messaggio + "nuovamente impostare i turni di prenotazione. \nI turni precedenti sono stati eliminati perchè si riferivano ad una data di prenotazione differente \n"
                    alert(messaggio)
                    reference = "/data-prenotazione-modificata/" + this.pk +"/"
                    location.href = reference;
//                    this.tornaIndietro()
                    }
                else {
                    alert("Gentile utente, la sua prenotazione è stata modificata correttamente")
                    this.tornaIndietro()
                    }
            }
        },

        SetStatusField() {
            if(this.data_prenotazione != this.previousData_Prenotazione) {
                this.status = "DC"; }
            if(this.numero_accompagnatori != this.previousNumero_Accompagnatori) {
                this.status = "DC";    }
            if(this.numero_totale_alunni != this.previousNumero_Totale_Alunni) {
                this.status = "DC";    }
          },


    },
        created() {
//     Controlla il titolo e il pulsante del Form
            if (this.pk)  {
                this.title = "Modifica Prenotazione"
                document.title = this.title;
            } else {
                this.title = "Aggiungi Prenotazione"
                document.title = this.title;
            }
            this.getTurni()
//              Controlla le labels dei Form
            if (this.scuola == true) {
                this.label_numero_accompagnatori = "Numero Accompagnatori"
            } else {
                this.label_numero_accompagnatori = "Numero Persone"
            }

            this.getDistinctDataTurni()
            this.getScuole()
            this.setRequestUserName()
//          IMPOSTA IL TIPO DI OPERAZIONE
            if (this.previousData_Prenotazione) {
                this.tipoOperazione ="update"}
            else {
                this.tipoOperazione ="insert"
            }


        //        this.getLastPrenotazione()
        },

};
</script>

<style lang="css" scoped>
</style>
