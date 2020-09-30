<template lang="html">
  <!-- DESCRIZIONE  PRENOTAZIONE EFFETTUATA -->
  <div class="container" id="da_stampare">

      Reset Password


      <form @submit.prevent="onSubmit" >
 <!--    Nome
        <label for="nome" class="col-3" >nome</label>
        <input type="text" class="col-9"  v-model="nome" id="nome  " autofocus>

        <label for="cognome" class="col-3" >Cognome</label>
        <input type="text" class="col-9"  v-model="cognome" id="cognome  " autofocus>

        <label for="email" class="col-3" >Indirizzo E-mail</label>
        <input type="text" class="col-9"  v-model="email" id="email  " autofocus>
 -->
        <br> <br>
        <button
          class = 'btn btn-success'
          type="submit"
          > Invia Link per il reset della password
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
  name: "UserResetPassword",


  data() {
    return {
     currentUser:{},
     nome:null,
     cognome:null,
     email:null,
     ruolo:null,
     telefono:null,
     fax:null,
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
            name: "mail"
        })
     },


     onSubmit() {
        location.href = "http://127.0.0.1:8000/mail/";
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
  },
  async created() {
//    document.title = "User Editor";
//    this.getUserName();


  }
};
</script>

<style lang="css" scoped></style>
