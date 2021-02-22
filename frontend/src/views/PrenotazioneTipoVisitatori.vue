<template lang="html">
    <div class="container mt-2 text-left">
        <div class="row">
            <div class="col-12">
           
              <div class="container ml-5">
                <a href="#"
                @click="gruppi"
                class="btn btn-primary btn-lg active" role="button" aria-pressed="true">Scuola/Gruppi
                </a>
                <a
                @click="privati"
                href="#" class=" ml-4 btn btn-secondary btn-lg active" role="button" aria-pressed="true">
                Privati </a>
                   <h2 class ="mt-3 mb-3">  Tipo di Visitatore:
                    <strong> {{descrizioneTipoVisitatore}} </strong> </h2>
                    <p>  </p>
                 </div>
                
                <form  @submit.prevent="onSubmit" >
                <br>
                <br>
                <br>
                    <button
                        class ="btn btn-outline-primary"
                        type="submit"
                        :disabled="disableButtomAvanti"
                        >Avanti
                    </button>
                    <button
                    @click="tornaIndietro"
                    class="btn btn-outline-info ml-3">Torna indietro
                    </button>

                </form>
            </div>
        </div>
    </div>
</template>

<script>


export default {
    name: "PrenotazioneTipoVisitatori",
  props: {
        tipoVisita: {
            type: String,
            required:false
        },

         scuola: {
            type: Boolean,
            required:false
        },


        from_Name: {
            type: String,
            required:false
        },
    },
  
    data() {
        return {
            descrizioneTipoVisitatore : null,
            scuolaImpostata:null,
            disableButtomAvanti: true,
            error: null,
        }
    },

       async beforeRouteEnter(to,from,next) {
        to.params.from_Name = from.name
    
        return next();
       },

    methods : {
       tornaIndietro() {
           this.$router.push({
                name: "prenotazione-tipovisita",
                params: { tipoVisita: this.tipoVisita, scuola:this.scuola }
            })
         },

        gruppi() {
            this.scuolaImpostata =true
            this.descrizioneTipoVisitatore = "Scuola/Gruppo"
            this.disableButtomAvanti = false
          
        },
        privati() {
        this.scuolaImpostata =false
        this.descrizioneTipoVisitatore = "Privato"
        this.disableButtomAvanti = false
        },



         async onSubmit() {
                this.$router.push({
                name: "prenotazione-editor",
                params: { tipoVisitaFromTipoVisitaForm: this.tipoVisita,scuolaFromTipoVisitatoriForm: this.scuolaImpostata }
            })
         },

        },
        created() {
        document.title = "Tipo Visitatori";
     
        if (this.from_Name === "prenotazione-editor") {
              this.disableButtomAvanti = false
          }
        
        
        if (this.from_Name === "prenotazione-tipovisita") {
              this.descrizioneTipoVisitatore = ""
        }
      
      if (this.scuola ) {
          this.descrizioneTipoVisitatore = "Scuola/Gruppo" 
          this.disableButtomAvanti = false
          this.scuolaImpostata =true
          return
        }

        
          if (this.scuola === false) {
              this.descrizioneTipoVisitatore = "Privato" 
              this.scuolaImpostata =false   
            }

        
      
        }
    }

</script>

<style lang="css" scoped>
</style>
