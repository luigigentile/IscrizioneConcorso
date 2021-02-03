<template lang="html">
    <div class="container mt-2 text-left">
        <div class="row">
            <div class="col-12">
                <h4 class = "mb-3">Sei sicuro di voler eliminare la seguente  prenotazione e tutti i suoi turni</h4>
                <form @submit.prevent="onSubmit" >
                    <h3
                        class = "form-control"
                        rows="3" cols="80">
                        Data: {{prenotazione.data_prenotazione}} - Accompagnatori: {{ prenotazione.numero_accompagnatori}} -  Numero Totale Alunni: {{prenotazione.numero_totale_alunni}}
                    </h3>
                    <br>
                    <button
                       class ="btn btn-outline-success"
                        type="submit"
                        >si, sono sicuro
                    </button>
                    <button
                    @click="tornaIndietro"
                    class="btn btn-outline-info ml-3">"No, torna indietro"
                    </button>

                </form>
            </div>
        </div>
    </div>
</template>

<script>

import { apiService } from "../common/api.service";
export default {
    name: "PrenotazioneConfirmDelete",
    props: {
        prenotazione: {
        type: Object,
        required:true
        },

    },

    data() {
        return {
            error: null,
        }
    },


    methods : {
        tornaIndietro() {
            this.$router.push({
                name: "Home",
            })
         },

         async onSubmit() {
             let  endpoint = `/api/prenotazioni/${this.prenotazione.id}/`;
             try {
             await apiService(endpoint,"DELETE");
             alert("La Prenotazione è stata eliminata con successo")
                this.$router.push({
                    name: "Home",
                })

             }catch {
             console.log("errore ");
             }

         },

        },
        created() {
            document.title = "Elimina Prenotazione";
        }
    }

</script>

<style lang="css" scoped>
</style>
