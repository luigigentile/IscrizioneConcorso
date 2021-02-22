<template lang="html">
  <div class="container text-left">
      <h4 class="d-none d-print-block">Padova {{ dataAttuale}} </h4>
<!--    SELEZIONA IL SETTORE  CON SELECT     -->
<div class ='d-print-none'>
    <label for="settore" class='mr-1'>Settore </label>
    <select  id="settore"
        class="col-3 mr-2"
        placeholder="settore"
        v-on:change="getVideoFilteredBySettore"
        v-model="selectedSettore">
        <option value="">All.....</option>
         <option
           v-for="settore in settori"
           :key="settore.id"
           :value=settore.id
           >{{ settore.settore }}
        </option>
    </select>
</div>


<!--    SELEZIONA LO STATUS  CON SELECT  
    <label for="idstatus" class='mr-1'>Status</label>
    <select  id="idstatus"
     class="col-3"
     placeholder="status"
     v-on:change="getPrenotazioniFilteredByStatus"
     v-model="status">
         <option value="">All.....</option>
         <option value="DC">Da Confermare</option>
         <option value="CO" selected>Confermato</option>
    </select>
</div>
  -->
    <!--       
     <h3 id="elencoVideo" >Elenco Video disponibili </h3>

     <video width="320" height="240" controls>
    <source src="https://www.youtube.com/watch?v=xpojsC7Qxzk&ab_channel=SperimentandoAPS.mp4"
     type="video/mp4">
  </video>
 -->
  

    
 
    <!--    INTESTAZIONE DELLE COLONNE    -->
        <div class="row border-bottom border-secondary mb-2">
        <div class="col-md-2 ">Titolo</div>
        <div class="col-md-4 ">Descrizione</div>
        <div class="col-md-2 ">Settore</div>
         </div>

   <!--    Elenco Video    -->
    <font face="Times New Roman" size="2" color="#000000">
    <div class="container border-bottom" v-for="(video) in videos_filtered"   :key="video.id">
        <div class="row">
            <div v-on:click="riproduciVideo(video.collegamento)" class="col-md-2 " v-text="video.titolo"> </div>
            <div class="col-md-4 " v-text="video.descrizione"> </div>
            <div class="col-md-2 " v-text="getDescrizioneSettoreTurno(video.settore)"> </div>
            <a class="btn btn-outline-success  btn-sm mb-2"  @click="riproduciVideo(video.collegamento)"
            >Visualizza
            </a>
          </div>
    </div>
    </font>
        <!--    Fine Elenco Video    -->

  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";


export default {
  name: "ElencoVideo",

  data() {
    return {
    videos: [],
    turni: [],
    videos_filtered: [],
    allVideo: [],
    settori:[],
    dataAttuale:null,
    selectedSettore : null,
    };
  },


  methods: {
    riproduciVideo(linkToVideo) {
      //alert(linkToVideo)
         window.open(linkToVideo,"mzwindows","location=0");
        },

      getSettoreTurno(IdTurno) {
   //     var settore= this.settori[IdTurno-1]
        alert(this.settori[IdTurno-1]["id"])
        return this.settori[IdTurno-1];
    },

    getDescrizioneSettoreTurno(varIdTurno) {
          var j,descrizioneSettoreTurno;
           for (j=0; j<this.settori.length; j++) {
            if (this.settori[j].id == varIdTurno) {
                  descrizioneSettoreTurno = this.settori[j].settore
              }
          }
          return (descrizioneSettoreTurno)
        },



    getSettori() {
          let endpoint = `/api/settori/`;
          apiService(endpoint).then(data => {
            this.settori.push(...data.results);
        });
    },

      getTurni() {
          let endpoint = `/api/turni/`;
          apiService(endpoint).then(data => {
            this.turni.push(...data.results);
        });
    },
     

     getAllVideo() {
      let endpoint = `/api/video/`;
     apiService(endpoint).then(data => {
        this.videos.push(...data.results);
         });
         this.videos_filtered = this.videos;
    },

    getVideoFilteredBySettore() {
        this.videos_filtered = [];
        if (this.selectedSettore != "" ) {
            for (var i =0 ; i<this.videos.length ;i++) {
              if (this.videos[i].settore == this.selectedSettore){
                this.videos_filtered.push(this.videos[i])
              }
            };
          }
           else  {
             this.videos_filtered = this.videos;
            }
    },
  },

  created() {
    this.getAllVideo() 
    this.getSettori();
    this.getTurni();
  
    //        document.getElementById('SelectUser').selectedIndex  = "1"
    document.title = "Elenco Video";
    this.dataAttuale = new Date();
  }
};
</script>
