import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./views/Home.vue";
import Prenotazione from "./views/Prenotazione.vue";
import PrenotazioneEditor from "./views/PrenotazioneEditor.vue";
import MovimentoPrenotazioneConfirmDelete from "./views/MovimentoPrenotazioneConfirmDelete.vue";
import RiepilogoPrenotazioni from "./views/RiepilogoPrenotazioni.vue";
import ElencoPrenotazioni from "./views/ElencoPrenotazioni.vue";
import ElencoVideo from "./views/ElencoVideo.vue";
import PrenotazioneConfirmDelete from "./views/PrenotazioneConfirmDelete.vue";
import PrenotazioneTipoVisita from "./views/PrenotazioneTipoVisita.vue";
import PrenotazioneTipoVisitatori from "./views/PrenotazioneTipoVisitatori.vue";
import UserEditor from "./views/UserEditor.vue";
import UserResetPassword from "./views/UserResetPassword.vue";
import About from "./views/About.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },

  {
    path: "/api/prenotazioni/:pk/movimenti/",
    name: "prenotazione",
    component: Prenotazione,
    props: true
  },

  {
      path: "/prenotazioni/riepilogo/",
      name: "prenotazioni-riepilogo",
      component: RiepilogoPrenotazioni,
      props: true
    },

    {
        path: "/prenotazioni/elenco/",
        name: "prenotazioni-elenco",
        component: ElencoPrenotazioni,
        props: true
      },

      {
        path: "/elencovideo/",
        name: "elencovideo",
        component: ElencoVideo,
        props: true
      },

  {
      path: "/prenotazioni/movimento/:id/",
      name: "movimento-prenotazione-confirm-delete",
      component: MovimentoPrenotazioneConfirmDelete,
      props: true
    },

  {
    path: "/about",
    name: "About",
    component: About,
    props: false
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
//    component: () => import(/* webpackChunkName: "about" */ "./views/About.vue")
  },

{
    path: "/prenotazioni/:pk/",
    name: "prenotazione-editor",
    component: PrenotazioneEditor,
    props: true
},

{
  path: "/prenotazionetipovisita/",
  name: "prenotazione-tipovisita",
  component: PrenotazioneTipoVisita,
  props: true
},

{
  path: "/prenotazionetipovisitatori/",
  name: "prenotazione-tipovisitatori",
  component: PrenotazioneTipoVisitatori,
  props: true
},



{
  path: "/prenotazioni/:pk/",
  name: "prenotazione-delete",
  component: PrenotazioneConfirmDelete,
  props: true

},

{
  path: "/users/:pk/",
  name: "user-editor",
  component: UserEditor,
  props: true

},

{
  path: "/users/reset_password/",
  name: "user-reset-password",
  component: UserResetPassword,
  props: false

},

];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
