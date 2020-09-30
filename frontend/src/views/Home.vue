<template>
  <div class="home">
    <div class="container">
      <h2>Elenco Prenotazioni
        <router-link title="Inserisci una nuova Prenotazione"
                  :to="{ name: 'prenotazione-editor'}"
                  ><span>
                      <img  src="../assets/icon-addlink.svg" alt="Nuova Prenotazione">
                </span>
        </router-link>
        </h2>

         <!-- AGGIUNGE LE PRENOTAZIONI DELL'UTENTE USER -->
      <div v-for="prenotazione in prenotazioni" :key="prenotazione.pk">
        <div class="card  border-primary rounded mb-1">
          <div class="card-header">
            <router-link
              :to="{ name: 'prenotazione', params: {pk: prenotazione.id , prenotazione:prenotazione} }"
              class="prenotazione-link"
            >
              Data Prenotazione {{ getLocalDate(prenotazione.data_prenotazione) }}
          </router-link>

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
                :to="{ name: 'prenotazione-editor', params: { pk: prenotazione.id, } }"
                class="prenotazione-editor-link"
                title = "Modifica Prenotazione"
                ><img  @click="ModificaPrenotazione(prenotazione)" src="../assets/icon-changelink.svg" alt="Modifica">
            </router-link>


            <p class="mb-0">
              Prenotazione Effettuata da :
              <strong class="author-name">{{ prenotazione.user }}</strong>
            </p>
              Scuola/Gruppo : <strong class="author-name">   {{ prenotazione.nome_scuola }}</strong>
              <p>
              Status : <strong class="author-name">   {{ prenotazione.status }}</strong>
          </p>

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

  data() {
    return {
      prenotazioni: [],
      userName: null,
      classe:null,
      usersName: [],
      next: null,
      loadingPrenotazioni: false,
      requestUser: null,
      selectedUser: null,
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
