<template>
  <ion-page>
    <ion-header>
      <ion-toolbar color="primary">

        <ion-buttons slot="start">
          <ion-button @click="newPost">Nuovo post</ion-button>
        </ion-buttons>
        <ion-buttons slot="end">
          <ion-button @click="dashboard">Home</ion-button>
        </ion-buttons>
        <ion-buttons slot="end">
          <ion-button @click="logout">Logout</ion-button>
        </ion-buttons>
      </ion-toolbar>
    </ion-header>
    <ion-content :class="'ion-padding'" >
      <ion-list class="nascondi">
      <div v-if="data.length != 0" >
        <ion-card v-for="(animal, index) in data" :key="index">
          <div class="ion-content-scroll-host" >
          <ion-card-header>
            <ion-card-subtitle>Tipologia: {{ animal.tipologia }}</ion-card-subtitle>
            <ion-card-title>{{ animal.nome_animale }}</ion-card-title>
            <ion-img :style="{ width: '250px', height: '250px'}" :src="'data:image/;base64,'+animal.file"></ion-img>
          </ion-card-header>

          <ion-card-content>
            <ion-button @click="deletePost(animal._id)">
              Elimina post
            </ion-button>
            <ion-item >
              <ion-label >Razza</ion-label>
              <ion-text>{{ animal.razza }}</ion-text>
            </ion-item>
            <ion-item >
              <ion-label>Colore</ion-label>
              <ion-text>{{ animal.colore }}</ion-text>
            </ion-item>
            <ion-item>
              <ion-label>Taglia</ion-label>
              <ion-text>{{ animal.taglia }}</ion-text>
            </ion-item>
            <ion-item>
              <ion-label>Età</ion-label>
              <ion-text>{{ animal.anni }}</ion-text>
            </ion-item>
            <ion-item>
              <ion-label>Vaccinato</ion-label>
              <ion-text>{{ animal.vaccinato }}</ion-text>
            </ion-item>
            <ion-item>
              <ion-label>Regione</ion-label>
              <ion-text>{{ animal.regione }}</ion-text>
            </ion-item>
            <ion-item>
              <ion-label>Città</ion-label>
              <ion-text>{{ animal.citta }}</ion-text>
            </ion-item>
            <ion-item>
              <ion-label position="stacked">Descrizione</ion-label>
              <ion-text>{{ animal.descrizione }}</ion-text>
            </ion-item>
          </ion-card-content>

          <ion-card-header>
            <ion-card-subtitle>Contatto</ion-card-subtitle>
            <ion-card-title>{{ animal.creatore.nome }} {{ animal.creatore.cognome }}</ion-card-title>
          </ion-card-header>

          <ion-card-content>
            <ion-item>
              <ion-label position="stacked">Email</ion-label>
              <ion-text>{{ animal.creatore.email }}</ion-text>
            </ion-item>
            <ion-item>
              <ion-label position="stacked">Cellulare</ion-label>
              <ion-text>{{ animal.creatore.cellulare }}</ion-text>
            </ion-item>
          </ion-card-content>
          </div>
        </ion-card>
        </div>
        <div v-else>
          <h1 style="color:white;text-align:center;">Pubblica il tuo primo post</h1> 
        </div>
      </ion-list>
    </ion-content>
  </ion-page>
</template>
<script setup>
import {loadingController ,onIonViewWillEnter,IonButtons,IonButton,IonImg, IonCard, IonCardHeader, IonCardTitle, IonCardSubtitle, IonCardContent,IonToolbar,IonHeader,IonLabel,IonText,IonItem,IonList,IonContent,IonPage} from '@ionic/vue';
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from "vue-router";




const showLoading = async () => {
        const loading = await loadingController.create({
          message: 'Caricamento...',
          duration: 2000
        });
        
        loading.present();
      }
const load=ref({load:false})
const data = ref([]);
const router = useRouter();

const logout=()=>{
  localStorage.setItem("refresh","1"); //forzo il refresh
  localStorage.setItem("token",""); //rimuovo il token
  router.push("/auth")
  }

const newPost=()=>{router.push("/newPost")}
const dashboard=()=>{router.push("/dashboard")}
const getPosto = () =>{  
  axios.get('http://127.0.0.1:5000/getMyPost',{
    headers: {
      "Authorization": localStorage.getItem("token")
    }
  })
  .then( response => {
    if(response.status!=404)
    data.value=response.data
  })
  .catch(() => {
    console.log("Nessun post trovato");

  });}
  //refresh del profilo se richiesto e salvataggio del token
  onIonViewWillEnter(() => {

    if(!load.value.load){
      showLoading()
      load.value.load=true
    }
  if(localStorage.getItem("token")){

    if(localStorage.getItem("refresh")=="1")
    {
      localStorage.setItem("refresh","")
      window.location.reload()
    }
      
    getPosto()
  }

  else
  router.push("/auth")


});



const deletePost = (postId) => {
      
      axios.post('http://127.0.0.1:5000/deletePost',  {
        "id":postId
      },{
            headers: {
              "Authorization": localStorage.getItem("token"),
              "Content-Type": "multipart/form-data",
            
            }
        })
      .then(response => {
        if(response.status!=404)
        {//NON FUNZIONA PER MOBILE
          
          Notification.requestPermission()
         .then(permission => {
          if (permission === 'granted') {
            new Notification('Animaletto', {
              body: 'Post cancellato con successo!'
            });
          }
        });
          getPosto()
          window.location.reload()
        }
      })
      .catch(() => {
        console.error("");
      });
    }


</script>

<style scoped>
  ion-content {
    --background: url(../wall.jpg) 100% 100% no-repeat;
  }
  .nascondi
  {
    background-color: transparent;
  }
</style>