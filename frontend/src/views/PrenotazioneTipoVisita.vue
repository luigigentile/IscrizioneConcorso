<template lang="html">
    <div class="container mt-2 text-left">
        <div class="row">
            <div >
              
             <h2> La visita alla mostra puo' essere Virtuale o in Presenza </h2>
                     <p> La  <strong> visita guidata virtuale </strong> verrà effettuata tramite una videoconferenza con una nostra guida. 
                     <br>
                     <span> 
                     Per la  <strong> visita in presenza </strong> è sufficiente presentarsi all'ingresso della mostra 15 minuti prima dell'orario di prenotazione.</span>
                      <span class = "btn btn-outline-primary ml-4"
                      @click="visualizzaNormeAntiCovid"
                      >Norme Anticovid
                         </span>
                      </p>
             
              <div class="ml-5">
                <a href="#"
                    @click="virtuale"
                    class="btn btn-primary btn-lg active" role="button" aria-pressed="true">Virtuale
                    </a>
                    <a
                    @click="inPresenza"
                    href="#" class=" ml-4 btn btn-secondary btn-lg active" role="button" aria-pressed="true">In Presenza </a>
                    <h2 class ="mt-3 mb-3">  Tipo di Visita Selezionata:
                        <strong> {{descrizioneTipoVisita}} </strong> </h2>
                        <p>  </p>
                </div>
                <form @submit.prevent="onSubmit" >
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
    name: "PrenotazioneTipoVisita",
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
            descrizioneTipoVisita : null,
            tipoVisitaImpostata: null,
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
                name: this.from_Name
            })
         },

        visualizzaNormeAntiCovid() {
        var linkpage = "https://sperimentandoaps.wordpress.com/norme-per-la-visita-in-presenza-in-sicurezza/"
        window.open(linkpage,"");
        },

        virtuale() {
            this.descrizioneTipoVisita = "Virtuale"
            this.tipoVisitaImpostata ="VI"
            this.disableButtomAvanti = false
        },
        inPresenza() {
        this.descrizioneTipoVisita = "In Presenza"            
        this.tipoVisitaImpostata ="PR"
        this.disableButtomAvanti = false
        },

         async onSubmit() {
                this.$router.push({
                name: "prenotazione-tipovisitatori",
                params: { tipoVisita: this.tipoVisitaImpostata, scuola:this.scuola }
            })
         },

         },
        created() {
            document.title = "Tipo Visita";
          if (this.from_Name === "prenotazione-tipovisitatori") {
              this.disableButtomAvanti = false
           }


            if (this.tipoVisita =="VI") {
              this.descrizioneTipoVisita = "Virtuale"  
              this.tipoVisitaImpostata ="VI"
            }
            if (this.tipoVisita =="PR") {
              this.descrizioneTipoVisita = "In Presenza" 
              this.tipoVisitaImpostata ="PR"          
            }
        }
    }

</script>

<style lang="css" scoped>
</style>
