<template>
  <div class="home">
    <div class="container">
      <h2>Elenco Prenotazioni
        <router-link title="Inserisci una nuova Prenotazione"
                  :to="{ name: 'prenotazione-editor'}"
                  ><span>
                      <svg width="13" height="13" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                        <path fill="#70bf2b" d="M1600 796v192q0 40-28 68t-68 28h-416v416q0 40-28 68t-68 28h-192q-40 0-68-28t-28-68v-416h-416q-40 0-68-28t-28-68v-192q0-40 28-68t68-28h416v-416q0-40 28-68t68-28h192q40 0 68 28t28 68v416h416q40 0 68 28t28 68z"/>
                      </svg>
                </span>

        </router-link>
        </h2>

         <!-- AGGIUNGE LE PRENOTAZIONI DELL'UTENTE USER -->
      <div v-for="prenotazione in prenotazioni" :key="prenotazione.pk">
        <div class="card  border-primary rounded mb-1">
          <div class="card-header">

            <router-link  v-if="prenotazione.scuola || staff " title="Visualizza dettagli Prenotazione"
              :to="{ name: 'prenotazione', params: {pk: prenotazione.id , prenotazione:prenotazione} }"
              class="prenotazione-link"
            >
            Data Prenotazione {{ prenotazione.data_prenotazione }}
          </router-link>
          <span v-else>Data Prenotazione {{ prenotazione.data_prenotazione }} </span>

  <!--    icona delete      -->
              <router-link title="Elimina  Prenotazione"
                          :to="{ name: 'prenotazione-delete', params: {prenotazione:prenotazione} }"
                          ><span>
                              <svg width="14" height="14" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                                <path fill="#dd4646" d="M1490 1322q0 40-28 68l-136 136q-28 28-68 28t-68-28l-294-294-294 294q-28 28-68 28t-68-28l-136-136q-28-28-28-68t28-68l294-294-294-294q-28-28-28-68t28-68l136-136q28-28 68-28t68 28l294 294 294-294q28-28 68-28t68 28l136 136q28 28 28 68t-28 68l-294 294 294 294q28 28 28 68z"/>
                            </svg>
                            </span>
                </router-link>
    <!--    icona change     -->
            <router-link
                :to="{ name: 'prenotazione-editor', params: { pk: prenotazione.id, prenotazione:prenotazione} }"
                class="prenotazione-editor-link"
                title = "Modifica Prenotazione"
                > <svg width="13" height="13" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                  <path fill="#efb80b" d="M491 1536l91-91-235-235-91 91v107h128v128h107zm523-928q0-22-22-22-10 0-17 7l-542 542q-7 7-7 17 0 22 22 22 10 0 17-7l542-542q7-7 7-17zm-54-192l416 416-832 832h-416v-416zm683 96q0 53-37 90l-166 166-416-416 166-165q36-38 90-38 53 0 91 38l235 234q37 39 37 91z"/>
                </svg>
            </router-link>

            <p class="mb-0">
              Prenotazione Effettuata da :
              <strong class="author-name">{{ prenotazione.user }}</strong>
            </p>
            <div v-if="prenotazione.scuola" class="">
              Scuola/Gruppo : <strong class="author-name">   {{ prenotazione.nome_scuola }}</strong>

            </div>
            <div class="">
               <p> Status : <strong class="author-name">   {{ prenotazione.status }}</strong>
            </p>
              </div>

          </div>
          <div class="card-body mt-n3">
            <p v-if="prenotazione.scuola" class="mb-0">
              Numero Accompagnatori :
              <span class="author-name">{{
                prenotazione.numero_accompagnatori
              }}</span>
            </p>
            <p v-else class="mb-0">
              Numero persone :
              <span class="author-name">{{
                prenotazione.numero_accompagnatori
              }}</span>
            </p>

            <p v-if="prenotazione.scuola" class="mb-0">
              Numero Totale Alunni:
              <span class="author-name">{{
                prenotazione.numero_totale_alunni
              }}</span>
            </p>

            <p class="mb-0">
              Esigenze:
              <span class="author-name">{{ prenotazione.esigenze }}</span>
            </p>

            <!-- FINE AGGIUNGE LE DOMANDE POSTE DALL'UTENTE USER -->
          </div>
        </div>
      </div>


    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
import { FormatToLocalDateString } from "../common/methods.js";

export default {
  name: "Home",

  computed: {
    iconAddLink() {
      return require("../assets/icon-addlink.svg");
  }
  },

  data() {
    return {
      prenotazioni: [],
      userName: null,
      staff:false,
      classe:null,
      usersName: [],
      next: null,
      loadingPrenotazioni: false,
    };
  },

  methods: {
      getLocalDate(Data) {
    //    return new Date(DataPrenotazione).toLocaleDateString();
        return FormatToLocalDateString(Data);
          },

    getPrenotazioni() {
      let endpoint = "api/prenotazioni/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingPrenotazioni = true;
      apiService(endpoint).then(data => {
        this.prenotazioni.push(...data.results);
        this.loadingPrenotazioni = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },


   getUserName() {
            let endpoint = "api/user/";
            apiService(endpoint)
              .then(data => {
                 this.userName = data.username;
                 this.staff = data.is_staff;
              })
        },

    getNumeroPrenotati() {
        return 100

          },
  },
    created() {
      this.getPrenotazioni();
      this.getUserName();


    //            this.getUsersName();

    //        document.getElementById('SelectUser').selectedIndex  = "1"
    document.title = "Prenotazioni";
  }
};
</script>
