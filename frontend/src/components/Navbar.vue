<template lang="html">

  <nav class="navbar navbar-expand-sm navbar-light bg-light my-navbar">
    <div class="container">
      <router-link :to="{ name: 'Home' }" class="navbar-brand" title="Ritorna alla pagina principale">
        <span><img width="15%" :src="logoSperimentando" alt="mi piace"/>
         <img src="/static/logoSperimentandoPiccolo.jpeg" style = 'max-width:15%' ></span>
        Sperimentando
      </router-link>

      <img src="/static/logoSperimentandoPiccolo.jpeg" style = 'max-width:4%' >


      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item" title="Ritorna alla pagina principale">
            <router-link :to="{ name: 'Home' }" class="btn btn-sm btn-primary"
              >Home
            </router-link>
          </li>
  <!-- Nuova Prenotazione
          <li class="nav-item mx-1 mp-0">
            <router-link :to="{ name: 'prenotazione-editor' }" class="btn btn-sm btn-primary"
              >Nuova Prenotazione
            </router-link>
          </li>
      -->
      <!-- Elenco Prenotazioni -->
          <li class="nav-item mx-1 " title="Visualizza l'elenco delle prenotazioni">
            <router-link :to="{ name: 'prenotazioni-elenco' }" class="btn btn-sm btn-primary"
              >Elenco Prenotazioni
            </router-link>
          </li>
 <!-- Riepilogo Prenotazioni -->
          <li class="nav-item mx-1" >
            <router-link v-show="currentUser.isStaff" :to="{ name: 'prenotazioni-riepilogo' }" class="btn btn-sm btn-primary"
              >Riepilogo Prenotazioni
            </router-link>
          </li>


    <!-- Menu Utente Dropdown -->
      <div class="dropdown nav-item mx-1">
        <button class="btn btn-sm btn-info " type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
         {{userName}}:
         </button>
        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <div class="dropdown-item">
                <router-link
                  :to="{ name: 'user-editor',params: {pk: currentUser.id } }"
                  class="user-editor-link"
                >Dati Personali
                </router-link>
            </div>
            <a class="dropdown-item" href="/accounts/login/">Login</a>
            <a class="dropdown-item" href="/accounts/logout/">Logout</a>
            <a class="dropdown-item" href="/accounts/password_change/">Cambio Password</a>
        </div>
      </div>

    <!-- Menu Admin -->
      <div class="dropdown" v-show="currentUser.isStaff">
        <button class="btn btn-sm btn-info " type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        Tabelle
        </button>
        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
             <a class="dropdown-item" href="/admin/prenotazioni/anagraficascuole/">Anagrafica Scuole</a>
             <a class="dropdown-item" href="/admin/users/customuser/">Utenti</a>
             <a class="dropdown-item" href="/admin/prenotazioni/tabellaturni/">Tabella Turni</a>
             <a class="dropdown-item" href="/admin/prenotazioni/tabellasettori/">Tabella Settori</a>
             <a class="dropdown-item" href="/admin/prenotazioni/tabellaruoli/">Tabella Ruoli</a>
            <a class="dropdown-item" href="/admin/sites/site/">Siti</a>
            <a class="dropdown-item" href="/admin/prenotazioni/prenotazione/">Prenotazioni </a>
            <a class="dropdown-item" href="/admin/prenotazioni/movimentiprenotazione/">Dettaglio Prenotazioni </a>
            </div>
      </div>
 <!-- Pulsante About-->
           <li class="nav-item mx-1">
             <router-link :to="{ name: 'About' }" class="btn btn-sm btn-info"
               >About
             </router-link>
           </li>


        </ul>
      </div>
    </div>
    <!--container -->
  </nav>
</template>

<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>


<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "NavbarComponent",

  computed: {
    logoCM() {
      return require("../assets/logo.png");
  },
    logoSperimentando() {
      return require("../assets/logoSperimentandoPiccolo.jpeg");
    }

},

    data() {
        return {
            userName:null,
            currentUser:{},
        };
    },

    methods: {
      getLocalDate(Data) {
        return "local data"
    },

    getUserName() {
            this.currentUser = {};
             let endpoint = "api/user/";
             apiService(endpoint)
               .then(data => {
                 this.currentUser.id = data.id;
                 this.currentUser.userName = data.username;
                 this.currentUser.isStaff = data.is_staff;
                 this.userName=data.username;
                window.localStorage.setItem("username", data.username);
                window.localStorage.setItem("isStaff", data.is_staff);
               })
         },

  },

    created() {
        this.getUserName();
     }

};



</script>


<style lang="css">
.my-navbar {
  border-bottom: 1px solid #ddd;
}

.navbar-brand {
  font-weight: bold;
  font-size: 130%;
}

.navbar-brand:hover {
  color: #dc3545 !important;
}
</style>
