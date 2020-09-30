<template lang="html">
    <div class="container mt-2">
        <div class="row">
            <div class="col-12">
                <h3 class = "mb-3">Sei sicuro di voler eliminare la seguente domanda </h3>

                <form @submit.prevent="onSubmit" >

                    <h3
                        class = "form-control"
                        rows="3" cols="80">
                        {{question.content}}
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
    name: "ConfirmDelete",
    props: {
        question: {
        type: Object,
        required:true
        },
    },

    data() {
        return {
            error: null,
            usersName:[],
        }
    },

    methods : {
        tornaIndietro() {
        this.$emit("confirm-delete",null);
         },

         async onSubmit() {
             this.$emit("confirm-delete",this.question.slug);
        },
    },
        created() {
            document.title = "Add Question";
        }
    }

</script>

<style lang="css" scoped>
</style>
