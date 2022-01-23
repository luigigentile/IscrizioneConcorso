<template lang="html">
    <div class="container text-left">
<!--    TITOLO - Pulsante Dettaglio Prenotazione - pulsante Pagamenti -->
        <div class="container " >
            <div class="row  rounded" >
                <div class="col-md-5" >
                      <h2 >{{title}}  </h2>
                </div>
                 
              <!--   Pulsante Dettaglio Prenotazione 
                <div class="col-md-3 mt-2 text-right" >
                     <span class="text-right" v-if="scuola && pk">
                     <router-link   title="Visualizza dettagli Prenotazione"
                       :to="{ name: 'prenotazione', params: {pk: prenotazione.id , prenotazione:prenotazione} }"
                       class="btn btn-outline-dark btn-sm "
                       >Dettaglio Turni
                       </router-link>
                      </span>
                </div>
            -->


               <!--   Pulsante PAGAMENTI -->
                <div class="col-md-6 mt-2 text-right">
                    <a class="btn btn-outline-dark btn-sm" @click="visualizzaPagamenti"> 
                        Pagamenti
                    </a>
                </div>

                   <!--  telefono utente  
                <div class="col-md-2 mt-2 text-right">
                <font face="Times New Roman" size="2" color="#000000">
                     <span  for="telefono">  {{ getTelefono(prenotazione.username) }} </span>
                 </font>
                </div>
               -->
            
          
            </div>
        </div>
    <!--    FINE TITOLO ....... pulsante Pagamenti -->
        <form @submit.prevent="onSubmit" >
        <div class = "border-bottom border-secondary pb-1" v-if="userIsStaff && pk">
        <!--    checkbox  pagato -->
            <input class="ml-1" type="checkbox" id="pagato"  v-model="pagato" @change="updatePagato">
            <label class="ml-1" for="pagato"> Pagato </label>
        <!--    STATUS   -->
            <label class="ml-3" for="id_status">Status:</label>
            <select class="ml-1" name="status" id="id_status" v-model="status" @change="updateStatus">
                <option value="DC">Da Confermare</option>
                <option value="CO" selected>Confermato</option>
                <option value="EF" selected>Effettuata</option>
            </select>
        <!--    Pulsante Invia mail Informativa -->
        <a class="btn btn-outline-success ml-3 mt-n2 btn-sm" v-if="!mailInformativaInviata" @click="inviaMailInformativa"
            >invia Mail Informativa
        </a>
        <!--    Pulsante Invia mail di Conferma -->
        <a class="btn btn-outline-success ml-2 mt-n2 btn-sm" v-if="!mailConfermaInviata" @click="inviaMailConferma"
            >invia Mail Conferma
        </a>

            <!--    Pulsante Invia mail Informativa -->
         <span class="ml-3" >Mail Inviate:  </span>
      
      <!--    checkbox  Mail Informativa    -->
        <input class="ml-1"  type="checkbox" id="mailinformativa"  v-model="mailInformativaInviata">
        <label class="ml-1" for="mailinformativa"> Informativa </label>

          <!--    checkbox  Mail di Conferma    -->
        <input class="ml-1"  type="checkbox" id="mailConferma"  v-model="mailConfermaInviata">
        <label class="ml-1" for="mailConferma"> Conferma </label>
       

            <!--   EMAIL DELL'UTENTE -->
        <font face="Times New Roman" size="2" color="#000000">
        <label class="ml-4" for="mailConferma">  {{ getUserEmail(prenotazione.user) }} </label><br>
        </font>
        </div>
        

<!--    checkbox  Scuola    -->
        <label class="ml-3 mt-3" for="scuola"> scuola/gruppo 
        <input class="ml-1 " @change="updateScuola" type="checkbox" id="scuola"  v-model="scuola">
    </label><br>
<!--    TIPO VISITA   -->
    <label  class="col-3" for="id_tipovisita">Tipo Visita:</label>
    <select  class="col-5"  name="tipoVisita" id="id_tipovisita" v-model="tipoVisita">
        <option value="VI">Virtuale</option>
        <option value="PR" selected>Presenza</option>
    </select>
     <label  class="col-4" for="id_tipovisita"></label>


<!--    DATA PRENOTAZIONE CON SELECT    -->
        <label for="dataPrenotazione" class="col-3" >Data Prenotazione</label>
        <select  id="dataPrenotazione"
            @change="changeDataPrenotazione"
            class="col-5" placeholder="data prenotazione"
            v-model="data_prenotazione">
            <option
               v-for="turno in distinct_data_turni"
               :key="turno.id"
               >{{ turno.data }}
             </option>
        </select>
<!--    ORA PRENOTAZIONE  solo NO scuola
            <input type="time" class="col-2 " title = "Ora di prenotazione"  placeholder="hh:mm" v-model="ora_prenotazione" id="oraPrenotazione" >

   -->
       <span  v-if="!scuola && tipoVisita=='VI'">
            <label for="oraPrenotazione" class="col-2" >Ora Prenotazione</label>
            <select  id="oraPrenotazione"
                class="col-2" placeholder="ora prenotazione"
                v-model="ora_prenotazione">
                    <option  value = "08:00:00">  8:00-9:00   </option>
                    <option value = "09:00:00">  9:00-10:00    </option>
                    <option value = "10:00:00"> 10:00-11:00    </option>
                    <option value = "11:00:00"> 11:00-12:00    </option>
                    <option value = "12:00:00"> 12:00-13:00    </option>
                    <option value = "13:00:00"> 13:00-14:00    </option>
                    <option value = "14:00:00"> 14:00-15:00    </option>
                    <option value = "15:00:00"> 15:00-16:00    </option>
                    <option value = "16:00:00"> 16:00-17:00    </option>
                    <option value = "18:00:00"> 18:00 - Evento   </option>
               </select>
         </span>
  
  <span  v-if="!scuola && tipoVisita=='PR'">
            <label for="oraPrenotazione" class="col-2" >Ora Prenotazione</label>
            <select  id="oraPrenotazione"
                class="col-2" placeholder="ora prenotazione"
                v-model="ora_prenotazione">
                    <option value = "09:00:00">  9:00-10:00    </option>
                    <option value = "10:00:00"> 10:00-11:00    </option>
                    <option value = "11:00:00"> 11:00-12:00    </option>
                    <option value = "12:00:00"> 12:00-13:00    </option>
                    <option value = "15:00:00"> 15:00-16:00    </option>
                    <option value = "16:00:00"> 16:00-17:00    </option>
            </select>
         </span>



        <div v-if="scuola">
            <!--    Nome Scuola con casella di testo e Select  -->
            <label for="nomescuola" class="col-3" >Nome Scuola/Gruppo</label>
            <input type="text" class="col-4" placeholder="nome scuola/gruppo" v-model="nome_scuola" id="nomescuola" autofocus>
            <!--    SELEZIONA LA SCUOLA CON SELECT    -->
          
            <select  id="nomescuola" 
                class="col-4 ml-3"
                placeholder="nome scuola"
                v-model="nome_scuola">
                <option value=""  ></option>
                <option
                       v-for="scuola in scuole"
                       :key="scuola.codice_ministeriale"
                       >{{ scuola.sigla  }} - {{ scuola.nome_scuola }} - {{ scuola.comune }}
                </option>
            </select>
            
        </div>
 
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

               <!--    argomenti Preferiti    -->
                    <label for="argomentiPreferiti" class="col-3"  >Argomenti Preferiti </label>
                    <input type="text" class="col-8" title = "Inserire qui gli argomenti che si desidera affrontare durante la visita"  placeholder="Argomenti Preferiti" v-model="argomentiPreferiti" id="argomentiPreferiti" autofocus>
                     <a class="text-right btn btn-outline-dark btn-sm ml-2" @click="visualizzaMappaMostra"> 
                      Mappa </a>
     
                <!--    esigenze    -->
                    <label for="esigenze" class="col-3" >Esigenze</label>
                    <input type="text" title = "Inserire qui eventuali esigenze che si possono avere durante la visita" class="col-9" placeholder="esigenze" v-model="esigenze" id="esigenze" autofocus>
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
                    Torna indietro
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
        tipoVisitaFromTipoVisitaForm: {
        type: String,
        required:false
        },

        scuolaFromTipoVisitatoriForm: {
        type: Boolean,
        required:false
        },

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
        previousOra_Prenotazione: {
            type: String,
            required:false
            },

        previousscuola: {
            type: Boolean,
            required:false
            },
        previousMailInformativa: {
            type: Boolean,
            required:false
            },

         previousMailConferma: {
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
        previousTipoVisita: {
        type: String,
        required:false
        },
        previousEsigenze: {
            type: String,
            required:false
            },
      previousArgomentiPreferiti: {
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
            ora_prenotazione:this.previousOra_Prenotazione || null,
            scuole: [],
            users:[],
            scuola:this.previousscuola || this.scuolaFromTipoVisitatoriForm,
            mailInformativaInviata:this.previousMailInformativa || false,
            mailConfermaInviata:this.previousMailConferma || false,
            pagato:this.previouspagato || false,
            nome_scuola:this.previousNome_Scuola || null,
            status:this.previousStatus || null,
            tipoVisita:this.previousTipoVisita || this.tipoVisitaFromTipoVisitaForm,
            numero_accompagnatori: this.previousNumero_Accompagnatori  || 1,
            numero_totale_alunni: this.previousNumero_Totale_Alunni  || 0,
            esigenze: this.previousEsigenze  || null,
            argomentiPreferiti: this.previousArgomentiPreferiti  || null,
            error: null,
            requestUserName : null,
            email:null,
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
                        to.params.previousOra_Prenotazione = data.ora_prenotazione;
                        to.params.previousscuola = data.scuola;
                        to.params.previousMailInformativa = data.mailInformativaInviata;
                        to.params.previousMailConferma = data.mailConfermaInviata;
                        to.params.previouspagato = data.pagato;
                        to.params.previousNome_Scuola = data.nome_scuola;
                        to.params.previousStatus = data.status;
                        to.params.previousTipoVisita = data.tipoVisita;
                        to.params.previousNumero_Accompagnatori = data.numero_accompagnatori;
                        to.params.previousNumero_Totale_Alunni = data.numero_totale_alunni;
                        to.params.previousEsigenze = data.esigenze;
                        to.params.previousArgomentiPreferiti = data.argomentiPreferiti;
                    })
                    .catch(error => console.log(error))
            }
//              if(to.params.pk == undefined) {
//                 to.params.previousscuola  = true
//              }
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
       
       TipoVisitaInPresenza() {
           var  anno = this.data_prenotazione.substring(6,10);
            var mese = this.data_prenotazione.substring(3,5);
            var giorno = this.data_prenotazione.substring(0,2);
            var data = new Date(anno, mese, giorno);
        //  MODIFICA EFFETTUATA IL 25 O4 2021 PER PERMETTERE ANCHE LE PRENOTAZIONI DI SABATO E DOMENICA
            if((data.getDay() == 2 || data.getDay() == 3)   && this.tipoVisita == "??") {
             return false
            }
            return true
           },
        
        changeDataPrenotazione() {
             if(!this.TipoVisitaInPresenza() ) {
            alert("Attenzione per le norme anti Covid non puoi effettuare una visita in Presenza di Sabato o di Domenica. \n Cambia la data di prenotazione")
            document.getElementById('dataPrenotazione').focus();
            return
            }

            if (this.scuola && this.tipoOperazione =="update") {
                var messaggio
                messaggio = "Gentile utente, le ricordiamo che se viene modificata la data di . \n"
                messaggio = messaggio + "prenotazione dovrà impostare nuovamente i turni di prenotazione perchè il sistema \n"
                messaggio = messaggio + "dovrà controllare la disponibilità di posti. \n"
                alert(messaggio)
                }
            },

 //          UPDATE PAGATO        
        updatePagato() {
            let endpoint = `/api/prenotazioni/${this.pk}/`;
            apiService(endpoint, "PUT", {data_prenotazione: this.data_prenotazione,
                                        pagato:this.pagato,
            })
        },
//          UPDATE Stato PRENOTAZIONE        
        updateStatus() {
            let endpoint = `/api/prenotazioni/${this.pk}/`;
            apiService(endpoint, "PUT", {data_prenotazione: this.data_prenotazione,
                                         status:this.status,
            })
        },
        
        
        inviaMailConferma() {
            var reference
    //          SALVA LA PRENOTAZIONE
            this.SetStatusField();
            let endpoint = `/api/prenotazioni/${this.pk}/`;
            this.mailConfermaInviata = true
            apiService(endpoint, "PUT", {data_prenotazione: this.data_prenotazione,
                                        scuola:this.scuola,
                                        mailInformativaInviata:this.mailInformativaInviata,
                                        mailConfermaInviata:this.mailConfermaInviata,
                                        pagato:this.pagato,
                                        nome_scuola:this.nome_scuola,
                                        status:this.status,
                                        tipoVisita:this.tipoVisita,
                                        numero_accompagnatori: this.numero_accompagnatori,
                                        numero_totale_alunni:this.numero_totale_alunni,
                                        esigenze:this.esigenze,
                                        argomentiPreferiti:this.argomentiPreferiti,
                                        })
            alert("La prenotazione è stata modificata correttamente \ned è stata inviata una mail di conferma all'utente: " + this.requestUserName)
            reference = "/mail-conferma-prenotazione/" + this.pk +"/"
            location.href = reference;
           
          },

          
          inviaMailInformativa() {
            var reference
    //          SALVA LA PRENOTAZIONE
            this.SetStatusField();
            let endpoint = `/api/prenotazioni/${this.pk}/`;
            this.mailInformativaInviata = true
            apiService(endpoint, "PUT", {data_prenotazione: this.data_prenotazione,
                                        scuola:this.scuola,
                                        mailInformativaInviata:this.mailInformativaInviata,
                                        mailConfermaInviata:this.mailConfermaInviata,
                                        pagato:this.pagato,
                                        nome_scuola:this.nome_scuola,
                                        status:this.status,
                                        tipoVisita:this.tipoVisita,
                                        numero_accompagnatori: this.numero_accompagnatori,
                                        numero_totale_alunni:this.numero_totale_alunni,
                                        esigenze:this.esigenze,
                                        argomentiPreferiti:this.argomentiPreferiti,
                                        })
            alert("La prenotazione è stata modificata correttamente \ned è stata inviata una mail di conferma all'utente: " + this.prenotazione.user)
            reference = "/mail-informativa/" + this.pk +"/"
            location.href = reference;
           
          },

        visualizzaPagamenti() {
              var linkpage = "https://sperimentandoaps.wordpress.com/pagamenti-mostra-20-21/"
              window.open(linkpage,"");
        },

        visualizzaMappaMostra() {
              var linkpage = "https://sperimentandoaps.wordpress.com/mappa-sperimentando-20-21/"
              window.open(linkpage,"");
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
        getUsers() {
              let endpoint = `/api/users/`;
              apiService(endpoint).then(data => {
                this.users.push(...data.results);
            });
        },

          getUserEmail(username) {
           for (var i=0; i<this.users.length ;i++) {
              
            if (this.users[i].username == username ) {
                return  this.users[i].email
            }
           }
        },


        getTelefono(username) {
           for (var i=0; i<this.users.length ;i++) {
              
            if (this.users[i].username == username ) {
                return  this.users[i].telefono
            }
           }
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
                name: this.from_Name,
                params: { scuola: this.scuola, tipoVisita:this.tipoVisita }
            })
         },

          goToHome() {
            this.$router.push({
                name: "Home"
              })
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
                                               mailInformativaInviata:this.mailInformativaInviata,
                                               mailConfermaInviata:this.mailConfermaInviata,
                                               pagato:this.pagato,
                                               nome_scuola:this.nome_scuola,
                                               status:this.status,
                                               tipoVisita:this.tipoVisita,
                                               numero_accompagnatori: this.numero_accompagnatori,
                                               numero_totale_alunni:this.numero_totale_alunni,
                                               esigenze:this.esigenze,
                                               argomentiPreferiti:this.argomentiPreferiti,
                                               })
                                            }
                      },

        onSubmit() {
            var messaggio,reference
         // CONTROLLA CHE SIA INSERITA LA  DATA PRENOTAZIONE  
            if (this.data_prenotazione==null) {
                alert("Attenzione !!!! la data di prenotazione non puo' essere null")
                document.getElementById('dataPrenotazione').focus();
                return
            }
            // CONTROLLO CHE SIA INSERITO IL NOME DELLA SCUOLA  
            if (this.nome_scuola==null && this.scuola) {
                alert("Attenzione !!!! la Scuola o il gruppo non puo' essere null")
                document.getElementById('dataPrenotazione').focus();
                return
            }
            // CONTROLLA CHE NON SIA INSERITA UNA VISITA IN PRESENZA        
            if(!this.TipoVisitaInPresenza() ) {
            alert("Attenzione per le norme anti Covid non puoi effettuare una visita in Presenza di Sabato o di Domenica. \n Cambia la data di prenotazione")
            document.getElementById('dataPrenotazione').focus();
            return
            }
          //   INSERISCE UNA NUOVA PRENOTAZIONE
            if (!this.previousData_Prenotazione) {
                let endpoint = `/api/prenotazioni/`;
                apiService(endpoint, "POST", {data_prenotazione: this.data_prenotazione,
                                                ora_prenotazione: this.ora_prenotazione,
                                                numero_accompagnatori: this.numero_accompagnatori,
                                                scuola:this.scuola,
                                                tipoVisita:this.tipoVisita,
                                                mailInformativaInviata:this.mailInformativaInviata,
                                                mailConfermaInviata:this.mailConfermaInviata,
                                                nome_scuola:this. nome_scuola,
                                                numero_totale_alunni:this.numero_totale_alunni,
                                                esigenze:this.esigenze,
                                                argomentiPreferiti:this.argomentiPreferiti,
                                                })


                messaggio = "Gentile utente, \ngrazie di aver prenotato una visita alla mostra  Sperimentando.  \n"
                if (this.scuola) {
                    messaggio = messaggio + "Completi la prenotazione inserendo i turni e i settori da visitare.\n"
                }
                messaggio = messaggio + "Nei prossimi giorni Le manderemo una mail di conferma da parte di Sperimentando \n"
                messaggio = messaggio + "Distinti saluti,\nlo staff di Sperimentando"
                if (!this.scuola) { 
                    alert(messaggio)
                }
//        SI POSIZIONE SULL'ULTIMA PRENOTAZIONE O TORNA ALLA PAGINA home
                if (this.scuola) {
                    this.getLastPrenotazione()
                }else {
                    this.goToHome()
                }
//                this.vaiAMovimentiPrenotazione();
            }
 //         UPDATE  PRENOTAZIONE          
          if (this.previousData_Prenotazione) {
                this.SetStatusField();
//                Controlla che il nome della scuola non sia blank
                  if (this.nome_scuola == "") {
                      this.nome_scuola = null
                    }

//              UPDATE  PRENOTAZIONE            
                let endpoint = `/api/prenotazioni/${this.pk}/`;
                apiService(endpoint, "PUT", {data_prenotazione: this.data_prenotazione,
                                            ora_prenotazione: this.ora_prenotazione,
                                            scuola:this.scuola,
                                            mailInformativaInviata:this.mailInformativaInviata,
                                            mailConfermaInviata:this.mailConfermaInviata,
                                            pagato:this.pagato,
                                            nome_scuola:this.nome_scuola,
                                            status:this.status,
                                            tipoVisita:this.tipoVisita,
                                            numero_accompagnatori: this.numero_accompagnatori,
                                            numero_totale_alunni:this.numero_totale_alunni,
                                            esigenze:this.esigenze,
                                            argomentiPreferiti:this.argomentiPreferiti,
                                            })
               
               //  NEL CASO DI CAMBIO DELLA DATA DI PRENOTAZIONE 
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
          
          //     MODIFICA L'OGGETTO PRENOTAZIONE
                    alert("Gentile utente, la sua prenotazione è stata modificata correttamente")
                    this.prenotazione.numero_accompagnatori = this.numero_accompagnatori
                    this.prenotazione.numero_totale_alunni = this.numero_totale_alunni
                    this.prenotazione.esigenze = this.esigenze
                    this.prenotazione.argomentiPreferiti = this.argomentiPreferiti
                 
                   this.$router.push({
                    name: "prenotazione",
                    params: { pk: this.pk, prenotazione: this.prenotazione }
                })
//

//                    this.tornaIndietro()
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
                this.title = "Avanti"
                document.title = this.title;
            } else {
                this.title = "Avanti"
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
            this.getUsers()
            this.getUserEmail()
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
