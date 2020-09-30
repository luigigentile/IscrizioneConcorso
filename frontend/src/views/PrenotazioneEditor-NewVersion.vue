<template lang="html">
    <div class="container mt-2">
        <h1 class = "mb-3">{{title}}  </h1>
            <form @submit.prevent="onSubmit" >

<!--    TURNO
                <div v-for="turno in turni" v-bind:key="turno.id">
                  <button v-for="date in turno.data" :key="turno.id" v-once>
                     {{date}}
                  </button>
                </div>
    -->
                    <label for="dataPrenotazione" class="col-3" >Data Prenotazione</label>
                    <input   id="dataPrenotazione" type="date"  class="col-9" placeholder="data prenotazione"
                        v-model="data_prenotazione">
                        <br>

                    <label for="dataPrenotazione" class="col-3" >Data Prenotazione</label>
                    <select  id="dataPrenotazione"
                     class="col-9" placeholder="data prenotazione"
                     v-on:change="getDataPrenotazione"
                     v-model="data_prenotazione">
                      <option
                       v-for="turno in turni"
                       :key="turno.id"
                       >{{ turno.data }}
                   </option>
                    </select>

                    <br>


                    <label for="numeroAccompagnatori" class="col-3" >Numero Accompagnatori</label>
                    <input id="numeroAccompagnatori" type="number"  class="col-9" placeholder="numero_accompagnatori"
                    v-model.number="numero_accompagnatori">

                    <label for="numeroTotaleAlunni" class="col-3" >Numero Totale Alunni</label>
                    <input id="numeroTotaleAlunni" type="number"  class="col-9" placeholder="numero_totale_alunni"
                    v-model.number="numero_totale_alunni">

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


export default {
    name: "PrenotazioneEditor",
    props: {
        pk: {
            type: Number,
            required:true
        },
        previousId: {
            type: Number,
            required:false
            },
        previousData_Prenotazione: {
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
    },

    data() {
        return {
            title: null,
            submitText:"Aggiungi Prenotazione",
            id:this.previousId || null,
            data_prenotazione:this.previousData_Prenotazione || null,
            numero_accompagnatori: this.previousNumero_Accompagnatori  || null,
            numero_totale_alunni: this.previousNumero_Totale_Alunni  || null,
            esigenze: this.previousEsigenze  || null,
            error: null,
            usersName:[],
            turni: [],

        }
    },

    async beforeRouteEnter(to,from,next) {
        if(to.params.pk !== undefined) {
            let endpoint = `/api/prenotazioni/${to.params.pk}/`;
            await apiService(endpoint)
                    .then(data => {
                        to.params.previousData_Prenotazione = data.data_prenotazione;
                        to.params.previousNumero_Accompagnatori = data.numero_accompagnatori;
                        to.params.previousNumero_Totale_Alunni = data.numero_totale_alunni;
                        to.params.previousEsigenze = data.esigenze;

                    })
            }
            return next();
    },

    beforeRouteLeave (to, from, next) {
  const answer = window.confirm('Do you really want to leave? you have unsaved changes!')
  if (answer) {
    next()
  } else {
    next(false)
  }
},

    filters: {
      capitalize: function (value) {
        if (!value) return ''
        value = value.toString()
        return value.charAt(0).toUpperCase() + value.slice(1)
      }
  },



    methods : {

        getDataPrenotazione() {
            alert(this.data_prenotazione)
        },


        getTurni() {
              let endpoint = `/api/turni/`;
              apiService(endpoint).then(data => {
                this.turni.push(...data.results);
            });
        },


        tornaIndietro() {
            this.$router.push({
                name: "Home"
            })
//        window.history.back()
         },

        onSubmit() {
            if (!this.previousData_Prenotazione) {
                let endpoint = `/api/prenotazioni/`;
                alert(this.data_prenotazione.toISOString())
                apiService(endpoint, "POST", { data_prenotazione: this.data_prenotazione,
                                            numero_accompagnatori: this.numero_accompagnatori,
                                            numero_totale_alunni:this.numero_totale_alunni,
                                            esigenze:this.esigenze})
                alert("Prenotazione Aggiunta correttamente")
            }

            if (this.previousData_Prenotazione) {
                alert("aa")
                let endpoint = `/api/prenotazioni/${this.pk}/`;
                apiService(endpoint, "PUT", { data_prenotazione: this.data_prenotazione,
                                            numero_accompagnatori: this.numero_accompagnatori,
                                            numero_totale_alunni:this.numero_totale_alunni,
                                            esigenze:this.esigenze})
                alert("Prenotazione Modificata correttamente")
            }

        this.tornaIndietro()

        },

    },
    created() {
    this.getTurni();
        if (this.pk)  {
            this.title = "Modifica Prenotazione"
            document.title = this.title;
        } else {
            this.title = "Aggiungi Prenotazione"
            document.title = this.title;
        }
    },

};
</script>

<style lang="css" scoped>
</style>
