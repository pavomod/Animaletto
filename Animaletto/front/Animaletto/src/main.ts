import { createApp } from 'vue'
import App from './App.vue'
import router from './router';
import "./registerServiceWorker"
import { IonicVue } from '@ionic/vue';

/* Core CSS required for Ionic components to work properly */
import '@ionic/vue/css/core.css';

/* Basic CSS for apps built with Ionic */
import '@ionic/vue/css/normalize.css';
import '@ionic/vue/css/structure.css';
import '@ionic/vue/css/typography.css';

/* Optional CSS utils that can be commented out */
import '@ionic/vue/css/padding.css';
import '@ionic/vue/css/float-elements.css';
import '@ionic/vue/css/text-alignment.css';
import '@ionic/vue/css/text-transformation.css';
import '@ionic/vue/css/flex-utils.css';
import '@ionic/vue/css/display.css';

/* Theme variables */
import './theme/variables.css';
// Above the createApp() line

import { defineCustomElements } from '@ionic/pwa-elements/loader';


//inizio modifica
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";


const firebaseConfig = {
  apiKey: "AIzaSyAgK3JQn99YrlKpZJRzqHywvk0Fzpb_EpA",
  authDomain: "animaletto-7a838.firebaseapp.com",
  projectId: "animaletto-7a838",
  storageBucket: "animaletto-7a838.appspot.com",
  messagingSenderId: "92891756826",
  appId: "1:92891756826:web:26c5c0b58683ff394bd4a3",
  measurementId: "G-XLHYLGWWPE"
};


initializeApp(firebaseConfig);
//fine modifica

defineCustomElements(window);

const app = createApp(App)
  .use(IonicVue)
  .use(router);
  



router.isReady().then(() => {
  app.mount('#app');
});

