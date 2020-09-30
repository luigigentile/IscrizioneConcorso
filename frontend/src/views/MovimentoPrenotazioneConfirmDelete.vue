 <template lang="html">
    <div class="container mt-2">
        <div class="row">
            <div class="col-12">
                <h3 class = "mb-3">Sei sicuro di voler eliminare la seguente prenotazione</h3>
                    <form @submit.prevent="onSubmit" >
                    <h3
                        class = "form-control"
                        rows="3" cols="80">
                        Classe: {{prenotazione.classe}}   - Turno: {{prenotazione.turno.settore}} - Numero Alunni: {{prenotazione.numero_alunni}}
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
    name: "MovimentoPrenotazioneConfirmDelete",
    props: {
        prenotazione: {
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
                params: { pk: this.pk }
            })
//            window.history.back(0)
         },

         async onSubmit() {
             let  endpoint = `/api/movimentiPrenotazioni/${this.prenotazione.id}/`;
             alert(endpoint)
             try {
             await apiService(endpoint,"DELETE");
                this.$router.push({
                    name: "prenotazione",
                    params: { pk: this.pk, prenotazione:this.prenotazione}
                })

      //:to="{ name: 'prenotazione', params: {pk: prenotazione.id , prenotazione:prenotazione} }"


             }catch {
             console.log("err");
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
