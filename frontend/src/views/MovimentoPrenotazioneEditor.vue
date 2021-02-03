<template lang="html">
    <div class="container mt-2 text-left">
        <div class="row">
            <div class="col-12">
                <h1 class = "mb-3">{{title}} </h1>

                <form @submit.prevent="onSubmit" >
                   <input type="text" class="form-control" placeholder="name" v-model="turno" id="name" autofocus>
                    <input type="text" class="form-control" placeholder="name" v-model="classe" id="name" autofocus>
                    <input id="name" type="number"  class="form-control" placeholder="numero_alunni"
                    v-model.number="numero_alunni">

                    <br>
                    <button
                    class = 'btn btn-success'
                    type="submit"
                    > Aggiungi Prenotazione
                    </button>

                    <button
                    @click="tornaIndietro"
                    class="btn btn-sm btn-primary ml-3">
                    No, torna indietro
                    </button>


                </form>
                <p class = 'muted error mt-2'> {{ error }}</p>
                <p class='muted error mt-2'></p>
            </div>

        </div>

    </div>

</template>

<script>



import { apiService } from "../common/api.service";
export default {
    name: "MovimentoPrenotazioneEditor",
    props: {
        pk: {
        type: Number,
        required:false
        },
        previousTurno: {
        type: String,
        required:false
        },
        previousClasse: {
        type: String,
        required:false
        },
        previousNumero_Alunni: {
        type: Number,
        required:false
        },
    },

    data() {
        return {
            title: null,
            turno: this.previousTurno  || null,
            classe: this.previousClasse  || null,
            numero_alunni: this.previousNumero_Alunni  || null,
            error: null,
            usersName:[],

        }
    },

    async beforeRouteEnter(to,from,next) {
        if(to.params.slug !== undefined) {
            let endpoint = `/api/questions/${to.params.pk}/`;
            await apiService(endpoint)
                    .then(data => {
                        to.params.previousTurno = data.turno;;
                    })
            }
            return next();
    },
    methods : {
        tornaIndietro() {
            this.$router.push({
                name: "home"
            })
//                   window.history.back()
         },

        onSubmit() {
            if (!this.questionBody) {
                this.error = "Il campo non puo essere vuoto"
            } else if (this.questionBody.length > 240) {
                    this.error = "il campo non puo superare i 240 caratteri"
            } else {
                let endpoint = "/api/questions/";
                let method = 'POST';
                if (this.previousQuestion) {
                    method = 'PUT';
                    endpoint += `${this.slug}/`;
                }
                apiService(endpoint,method,{ content:this.questionBody })
                    .then(question_data => {
                        this.$router.push({
                            name:'question',
                            params: { slug: question_data.slug }

                        })
                    })
            };


            }
        },
        created() {
            if (this.slug)  {
                this.title = "Modifica Prenotazione"
                document.title = this.title;
            } else {
                this.title = "Aggiungi Prenotazione"
                document.title = this.title;
            }
        },
    }

</script>

<style lang="css" scoped>
</style>
