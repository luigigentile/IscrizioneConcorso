 <template lang="html">
    <div class="container mt-2 text-left">
        <div class="row">
            <div class="col-12">
                <h3 class = "mb-3">Sei sicuro di voler eliminare il seguente turno di prenotazione</h3>
                    <form @submit.prevent="onSubmit" >
                    <h3
                        class = "form-control"
                        rows="3" cols="80">
                        Classe: {{turnoPrenotazione.classe}}   - Turno: {{turnoPrenotazione.turno.settore}} - Numero Alunni: {{turnoPrenotazione.numero_alunni}}
                    </h3>
                    <br>
                    <button
                       class ="btn btn-outline-success"
                        type="submit"
                        >Si, sono sicuro
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
    name: "MovimentoPrenotazioneConfirmDelete",
    props: {
        prenotazione: {
        type: Object,
        required:true
        },
        turnoPrenotazione: {
        type: Object,
        required:true
        },
    pk: {
        type: Number,
        required: true
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
                name: "prenotazione",
                params: { pk: this.prenotazione.id, prenotazione:this.prenotazione }
            })
//            window.history.back(0)
         },

         async onSubmit() {
             let  endpoint = `/api/movimentiPrenotazioni/${this.turnoPrenotazione.id}/`;
             try {
             await apiService(endpoint,"DELETE");
                this.$router.push({
                    name: "prenotazione",
                    params: { pk: this.prenotazione.id, prenotazione:this.prenotazione}
                })

      //:to="{ name: 'prenotazione', params: {pk: prenotazione.id , prenotazione:prenotazione} }"


             }catch {
             console.log("err");
             }

         },

        },
        created() {
            document.title = "Elimina Turno Prenotazione";
        }
    }

</script>

<style lang="css" scoped>
</style>
