<template lang="html">
  <div class="container">
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
    <div class="container border-bottom" v-for="(video) in videos"   :key="video.id">
        <div class="row">
            <div v-on:click="riproduciVideo(video.collegamento)" class="col-md-2 " v-text="video.titolo"> </div>
            <div class="col-md-4 " v-text="video.descrizione"> </div>
            <div class="col-md-2 " v-text="getSettoreTurno(video.settore)"> </div>
            <a class="btn btn-outline-success  btn-sm"  @click="riproduciVideo(video.collegamento)"
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
import { FormatToLocalDateString } from "../common/methods.js";

export default {
  name: "ElencoVideo",

  data() {
    return {
    videos: [],
    allVideo: [],
    settori:[],
    dataAttuale:null,
    selectedSettore : null,
    firstFilter: true,
  };
  },


  methods: {
    riproduciVideo(linkToVideo) {
      //alert(linkToVideo)
         window.open(linkToVideo,"mzwindows","location=0");
        },

      getSettoreTurno(IdTurno) {
        return this.settori[IdTurno].settore;
    },

    getSettori() {
          let endpoint = `/api/settori/`;
          apiService(endpoint).then(data => {
            this.settori.push(...data.results);
        });
    },
   
      getLocalDate(Data) {
    //    return new Date(DataPrenotazione).toLocaleDateString();
        return FormatToLocalDateString(Data);
          },

      getToISOString(DataPrenotazione) {
    //    return new Date(DataPrenotazione).toLocaleDateString();
        return new Date(DataPrenotazione).toISOString();
          },


     getAllVideo() {
      let endpoint = `/api/video/`;
     apiService(endpoint).then(data => {
        this.videos.push(...data.results);
         });
    },

     getVideoFilteredBySettore() {
        alert(this.firstFilter)
          if (this.firstFilter) {
              this.allVideo = JSON.parse(JSON.stringify(this.videos));
              this.firstFilter = false
            }
            var len = this.videos.length
            alert("len=" + len)
            alert("settore:" + this.selectedSettore)
              for (var i = 0; i<= len; i++) {
                alert("i="+i)
                alert(this.videos[i].settore)
                   if (this.videos[i].settore != this.selectedSettore) {
//                if (this.allConnectivityRelay.edges[i].node.name != this.selectedName) { 
                    this.videos[i].splice(i,1);
                    i = i-1 
                    len = len-1
                 }
             }
       
        },  
 
  },

  created() {
    this.getAllVideo() 
    this.getSettori();
  
    //        document.getElementById('SelectUser').selectedIndex  = "1"
    document.title = "Elenco Video";
    this.dataAttuale = new Date();
  }
};
</script>
