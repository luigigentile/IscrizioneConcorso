<template lang="html">
  <!-- DESCRIZIONE  PRENOTAZIONE EFFETTUATA -->
  <div class="container text-left" id="da_stampare text-left">

 


      <form @submit.prevent="onSubmit" >
 <!--    Nome   -->
        <label for="nome" class="col-3" >Nome</label>
        <input type="text" class="col-9"  v-model="nome" id="nome  " autofocus>

        <label for="cognome" class="col-3" >Cognome</label>
        <input type="text" class="col-9"  v-model="cognome" id="cognome  " autofocus>

        <label for="email" class="col-3" >Email</label>
        <input type="text" class="col-9"  v-model="email" id="email  " autofocus>

        <label for="ruolo" class="col-3" >Ruolo</label>
        <input type="text" class="col-4"  v-model="ruolo" id="ruolo  " autofocus>

        
<!--    SELEZIONA LA SCUOLA CON SELECT    -->
        <select  id="nomeruolo"
        class="col-2 ml-3"
         placeholder="ruolo"
         v-model="ruolo">
        <option value=""></option>
         <option
               v-for="nomeruolo in ruoli"
               :key="nomeruolo.ruolo"
               >{{ nomeruolo.ruolo }}
        </option>
    </select>



        <label for="telefono" class="col-3" >Telefono</label>
        <input type="text" class="col-9"  v-model="telefono" id="telefono  " autofocus>

        <label for="fax" class="col-3" >Fax</label>
        <input type="text" class="col-9"  v-model="fax" id="fax" autofocus>
       
      
        <br> <br>
        <button
          class = 'btn btn-success'
          type="submit"
          > Conferma
        </button>

        <button
          @click="tornaIndietro"
          class="btn  btn-primary ml-3">
          No, torna indietro
        </button>

      </form>

  </div>

</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "UserEditor",

  props: {
    pk: {
      type: Number,
      required: false
    },
  },

  data() {
    return {
     currentUser:{},
     nome:null,
     cognome:null,
     email:null,
     ruolo:null,
     telefono:null,
     fax:null,
     ruoli: [],
    };
  },
  computed: {


  },

  methods: {

    setPageTitle(title) {
      document.title = title;
    },

    tornaIndietro() {
        this.$router.push({
            name: "Home"
        })
     },


     onSubmit() {
            let endpoint = `/api/usersviewset/${this.pk}/`;
             apiService(endpoint, "PUT", {first_name: this.nome,
                                         last_name:this.cognome,
                                         nome_scuola:this.nome_scuola,
                                         email:this.email,
                                         ruolo:this.ruolo,
                                         telefono: this.telefono,
                                         fax:this.fax,
                                         })
             alert("Dati Personali  Aggiornati Correttamente")
             this.tornaIndietro()
     },


    getUserName() {
            this.currentUser = {};
             let endpoint = `/api/usersviewset/${this.pk}/`;
             apiService(endpoint)
               .then(data => {
                 this.nome = data.first_name;
                 this.cognome = data.last_name;
                 this.email = data.email;
                 this.ruolo = data.ruolo;
                 this.telefono = data.telefono;
                 this.fax = data.fax;
                 })
         },

         getRuoli() {
               let endpoint = `/api/ruoli/`;
               apiService(endpoint).then(data => {
                 this.ruoli.push(...data.results);
             });
         },



  },
  async created() {
//    document.title = "User Editor";
    this.getUserName();
    this.getRuoli();

  }
};
</script>

<style lang="css" scoped></style>
