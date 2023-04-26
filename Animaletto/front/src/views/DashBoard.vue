<template>
  <ion-page>
    <ion-header>
      <ion-toolbar color="primary">
        <ion-title>Dashboard</ion-title>
        <ion-buttons slot="end">
          <ion-button @click="goToProfile">Profilo</ion-button>
        </ion-buttons>
      </ion-toolbar>
      
      <ion-toolbar class="filter-toolbar" :class="{ 'collapsed': isCollapsed }">
        <ion-buttons slot="start">
          <ion-button @click="toggleCollapse()">
            <span>Filtri</span>
          </ion-button>
        </ion-buttons>
        
        <ion-buttons slot="end">
          <ion-button @click="resetFilters()">
            <span>Applica</span>
          </ion-button>
        </ion-buttons>

        <ion-list v-show="!isCollapsed">
          
          <ion-item>
            <ion-label position="stacked">Regione</ion-label>
            <ion-select v-model="filters.regione">
              <ion-select-option value="">Tutte</ion-select-option>
              <ion-select-option value="Abruzzo">Abruzzo</ion-select-option>
              <ion-select-option value="Basilicata">Basilicata</ion-select-option>
              <ion-select-option value="Calabria">Calabria</ion-select-option>
              <ion-select-option value="Campania">Campania</ion-select-option>
              <ion-select-option value="Emilia Romagna">Emilia-Romagna</ion-select-option>
              <ion-select-option value="Friuli Venezia Giulia">Friuli-Venezia Giulia</ion-select-option>
              <ion-select-option value="Lazio">Lazio</ion-select-option>
              <ion-select-option value="Liguria">Liguria</ion-select-option>
              <ion-select-option value="Lombardia">Lombardia</ion-select-option>
              <ion-select-option value="Marche">Marche</ion-select-option>
              <ion-select-option value="Molise">Molise</ion-select-option>
              <ion-select-option value="Piemonte">Piemonte</ion-select-option>
              <ion-select-option value="Puglia">Puglia</ion-select-option>
              <ion-select-option value="Sardegna">Sardegna</ion-select-option>
              <ion-select-option value="Sicilia">Sicilia</ion-select-option>
              <ion-select-option value="Toscana">Toscana</ion-select-option>
              <ion-select-option value="Trentino Alto Adige">Trentino-Alto Adige/Südtirol</ion-select-option>
              <ion-select-option value="Umbria">Umbria</ion-select-option>
              <ion-select-option value="Valle d'Aosta">Valle d'Aosta/Vallée d'Aoste</ion-select-option>
              <ion-select-option value="Veneto">Veneto</ion-select-option>
            </ion-select>
          </ion-item>

          <ion-item>
            <ion-label position="stacked">Tipologia</ion-label>
            <ion-select v-model="filters.tipologia">
              <ion-select-option value="">Tutte</ion-select-option>
              <ion-select-option value="Cane">Cane</ion-select-option>
              <ion-select-option value="Gatto">Gatto</ion-select-option>
              <ion-select-option value="Criceto">Criceto</ion-select-option>
              <ion-select-option value="Coniglio">Coniglio</ion-select-option>
              <ion-select-option value="Uccello">Uccello</ion-select-option>
            </ion-select>
          </ion-item>

          <ion-item>
            <ion-label position="stacked">Taglia</ion-label>
            <ion-select v-model="filters.taglia">
              <ion-select-option value="">Tutte</ion-select-option>
              <ion-select-option value="Piccola">Piccola</ion-select-option>
              <ion-select-option value="Media">Media</ion-select-option>
              <ion-select-option value="Grande">Grande</ion-select-option>
            </ion-select>
          </ion-item>

          <ion-item>
            <ion-label position="stacked">Vaccinato</ion-label>
            <ion-select v-model="filters.vaccinato">
              <ion-select-option value="">Tutte</ion-select-option>
              <ion-select-option value="true">Sì</ion-select-option>
              <ion-select-option value="false">No</ion-select-option>
            </ion-select>
          </ion-item>
        </ion-list>
      </ion-toolbar>
    </ion-header>

    <ion-content :class="'ion-padding'">
      <ion-refresher slot="fixed" @ionRefresh="handleRefresh($event)">
        <ion-refresher-content></ion-refresher-content>
      </ion-refresher>
      <ion-list class="nascondi">
      <div v-if="data.length > 0">
        <ion-card v-for="(animal, index) in data" :key="index">
          <ion-card-header>
            <ion-card-subtitle>Tipologia: {{ animal.tipologia }}</ion-card-subtitle>
            <ion-card-title>{{ animal.nome_animale }}</ion-card-title>
            <div style="heigth:250px; width:250px;"><ion-img style="object-fit: cover;" :src="'data:image/;base64,'+animal.file" ></ion-img></div>
          </ion-card-header>

          
          <ion-card-content>
            
            <ion-item>
              <ion-label>Razza</ion-label>
              <ion-text>{{ animal.razza }}</ion-text>
            </ion-item>
            <ion-item>
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
              <br>
              <ion-button v-bind:href="'mailto:' + animal.creatore.email" expand="block">Email</ion-button>
              <br>
              <ion-button v-bind:href="'tel:' + animal.creatore.cellulare" expand="block">Chiama</ion-button>
            </ion-card-content>

        </ion-card>
      </div>
      <div v-else>
          <h1 style="color:white;text-align:center;">Nessun post da visualizzare</h1> 
      </div>
      </ion-list>
    </ion-content>
  </ion-page>
</template>



<script setup>
  import {onIonViewWillEnter,IonSelectOption,IonButtons,IonRefresher, IonRefresherContent,IonImg,IonButton, IonCard, IonCardHeader, IonCardTitle, IonCardSubtitle, IonCardContent,IonToolbar,IonHeader,IonTitle,IonLabel,IonText,IonItem,IonList,IonContent,IonPage,IonSelect,loadingController } from '@ionic/vue';
  import { ref } from 'vue';
  import axios from 'axios';
  import { useRouter } from "vue-router";



  const showLoading = async () => {
        const loading = await loadingController.create({
          message: 'Caricamento...',
          duration: 5000
        });
        
        loading.present();
      }
  //refresh della pagina quando viene effettuato un scroll verso il basso all'inizio della page
  const handleRefresh = (event) => {
      setTimeout(() => {
        window.location.reload()
        event.target.complete();
      }, 2000);
      return { handleRefresh };
    }
  const load = ref({load:false});
  const isCollapsed=ref({isCollapsed:false})
  const router = useRouter();
  const data = ref([]);
  //possibili filtri di ricerca
  const filters = ref({      
        regione: "",
        tipologia: "",
        taglia: "",
        vaccinato: ""});
  //append dei filtri per formare una query parametrizzata del tipo ?par&par1...
  const resetFilters = ()=>{
    let filtro="?"
    if(filters.value.regione!="")
      filtro+="regione="+filters.value.regione+"&"
    if(filters.value.tipologia!="")
      filtro+="tipologia="+filters.value.tipologia+"&"
    if(filters.value.taglia!="")
      filtro+="taglia="+filters.value.taglia+"&"
    if(filters.value.vaccinato!="")
      filtro+="vaccinato="+filters.value.vaccinato+"&"
    filtro=filtro.slice(0,-1) //rimuove l'and (&) finale.
    showLoading()
    getPosto(filtro)
  }

  const goToProfile =()=>{router.push("/profile")}
  //controllo del collapse del menu a tendina del filtri
  const toggleCollapse = () => {
  isCollapsed.value = !isCollapsed.value;
  }

  //richiede tutti i post presenti nel db
  const getPosto = (filtri) =>{
    
    if(filtri==undefined)
      filtri=""
    const back= 'http://127.0.0.1:5000/getPost'+filtri
    axios.get(back,{
      headers: {
        "Authorization": localStorage.getItem("token")
      }
    })
    .then( response => {
      if(response.status==200)
        data.value=response.data
      
    })
    .catch(()=> {
      console.log("");
    });}
    onIonViewWillEnter(() => {
    if(!load.value.load){
      showLoading()
      load.value.load=true
    }
    if(localStorage.getItem("token")){
      getPosto()
    }
    else
    router.push("/auth")
    
  });




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