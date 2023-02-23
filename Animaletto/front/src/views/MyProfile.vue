<template>
  <ion-page >
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
    <ion-content :class="'ion-padding'">
      <ion-list class="nascondi">
      <div v-if="data.length > 0">
        <ion-card v-for="(animal, index) in data" :key="index">
          <div class="ion-content-scroll-host" >
          <ion-card-header>
            <ion-card-subtitle>Tipologia: {{ animal.tipologia }}</ion-card-subtitle>
            <ion-card-title>{{ animal.nome_animale }}</ion-card-title>
            <ion-img :style="{ width: '250px', height: '250px'}" :src="'data:image/;base64,'+animal.file" ></ion-img>
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
          Pubblica il tuo primo post 
        </div>
      </ion-list>
    </ion-content>
  </ion-page>
</template>
<script setup>
import {IonButton,IonImg, IonCard, IonCardHeader, IonCardTitle, IonCardSubtitle, IonCardContent,IonToolbar,IonHeader,IonLabel,IonText,IonItem,IonList,IonContent,IonPage} from '@ionic/vue';
import { ref, onMounted } from 'vue';
import axios from 'axios';



const data = ref([]);

const logout=()=>{localStorage.setItem("token","");window.location.href = '/auth'}
const newPost=()=>{window.location.href = '/newPost'}
const dashboard=()=>{window.location.href = '/dashboard'}
const getPosto = () =>{  axios.get('http://192.168.248.104:5000/getMyPost',{
    headers: {
      "Authorization": localStorage.getItem("token")
    }
  })
  .then( response => {
    data.value=response.data
  })
  .catch(error => {
    console.log(error);
  });}
onMounted(() => {
  if(localStorage.getItem("token"))
    getPosto()
  else
  window.location.href = '/auth'
});

const deletePost = (postId) => {
      console.log(postId)
      axios.post('http://192.168.248.104:5000//deletePost',  {
        "id":postId
      },{
            headers: {
              "Authorization": localStorage.getItem("token"),
              "Content-Type": "multipart/form-data",
            
            }
        })
      .then(response => {
        if(response.status!=404)
        {
          getPosto()
          window.location.reload()
        }
      })
      .catch(error => {
        // show an error message, e.g.
        console.error(`Errore durante l'eliminazione del post ${postId}: ${error}`);
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