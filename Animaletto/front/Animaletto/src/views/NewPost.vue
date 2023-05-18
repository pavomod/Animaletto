<template>
    <ion-page>
      <ion-header>
        <ion-toolbar color="primary">
          <ion-title>Nuovo Post</ion-title>
          <ion-buttons slot="end">
            <ion-button @click="profile">Annulla</ion-button>
          </ion-buttons>
        </ion-toolbar>
      </ion-header>
      <ion-content class="ion-padding">
        
        <ion-list>
            <ion-item>
              <ion-label position="stacked">Regione</ion-label>
              <ion-select v-model="data.regione">
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
                <ion-label position="stacked">Citta</ion-label>
                <ion-input  v-model="data.citta"></ion-input>
            </ion-item>
            

            <ion-item>
              <ion-label position="stacked">Tipologia</ion-label>
              <ion-select v-model="data.tipologia">
                <ion-select-option value="Cane">Cane</ion-select-option>
                <ion-select-option value="Gatto">Gatto</ion-select-option>
                <ion-select-option value="Criceto">Criceto</ion-select-option>
                <ion-select-option value="Coniglio">Coniglio</ion-select-option>
                <ion-select-option value="Volatile">Volatile</ion-select-option>
                <ion-select-option value="Tartaruga">Tartaruga</ion-select-option>
                <ion-select-option value="Pesce">Pesce</ion-select-option>
                <ion-select-option value="Altro">Altro</ion-select-option>
              </ion-select>
            </ion-item>
            
            <ion-item>
                <ion-label position="stacked">Nome animale</ion-label>
                <ion-input v-model="data.nome_animale"></ion-input>
            </ion-item>
            
            <ion-item>
                <ion-label position="stacked">Razza</ion-label>
                <ion-input v-model="data.razza"></ion-input>
            </ion-item>


            <ion-item>
              <ion-label position="stacked">Taglia</ion-label>
              <ion-select v-model="data.taglia">
                <ion-select-option value="Piccola">Piccola</ion-select-option>
                <ion-select-option value="Media">Media</ion-select-option>
                <ion-select-option value="Grande">Grande</ion-select-option>
              </ion-select>
            </ion-item>

            <ion-item>
                <ion-label position="stacked">Colore</ion-label>
                <ion-select v-model="data.colore">
                  <ion-select-option value="Nero">Nero</ion-select-option>
                  <ion-select-option value="Marrone">Marrone</ion-select-option>
                  <ion-select-option value="Arancione">Arancione</ion-select-option>
                  <ion-select-option value="Bianco">Bianco</ion-select-option>
                  <ion-select-option value="Misto">Misto</ion-select-option>
                </ion-select>
              </ion-item>

            <ion-item>
                <ion-label position="stacked">Età</ion-label>
                <ion-select v-model="data.anni">
                  <ion-select-option value="0">0</ion-select-option>
                  <ion-select-option value="1">1</ion-select-option>
                  <ion-select-option value="2">2</ion-select-option>
                  <ion-select-option value="3">3</ion-select-option>
                  <ion-select-option value="4">4</ion-select-option>
                  <ion-select-option value="5">5</ion-select-option>
                  <ion-select-option value="6">6</ion-select-option>
                  <ion-select-option value="7">7</ion-select-option>
                  <ion-select-option value="8">8</ion-select-option>
                  <ion-select-option value="9">9</ion-select-option>
                  <ion-select-option value="10">10</ion-select-option>
                  <ion-select-option value="11">11</ion-select-option>
                  <ion-select-option value="12">12</ion-select-option>
                  <ion-select-option value="13">13</ion-select-option>
                  <ion-select-option value="14">14</ion-select-option>
                  <ion-select-option value="15">15</ion-select-option>
                </ion-select>
              </ion-item>
  
            <ion-item>
              <ion-label position="stacked">Vaccinato</ion-label>
              <ion-select v-model="data.vaccinato">
                <ion-select-option value="true">Sì</ion-select-option>
                <ion-select-option value="false">No</ion-select-option>
              </ion-select>
            </ion-item>

            <ion-item>
                <ion-label position="stacked">Descrizione</ion-label>
                <ion-input v-model="data.descrizione"></ion-input>
            </ion-item>
            <ion-item>
              <ion-label position="stacked">Carica una foto</ion-label>
              <IonInput type="file" accept="image/*" @change="handleChange" />
            </ion-item>

          </ion-list>
          <br><br><br>
          <ion-button expand="block" @click="publish">Pubblica</ion-button>
          <br><br><br><br><br>
      </ion-content>
    </ion-page>
  </template>
  
  <script>
  import axios from 'axios'
  import { defineComponent, ref } from "vue";
  import { loadingController,IonContent,IonPage,IonSelectOption,IonList,IonToolbar,IonHeader,IonTitle,IonButtons,IonItem, IonLabel, IonSelect, IonButton,IonInput } from "@ionic/vue";
  import { useRouter } from "vue-router";
  
  export default defineComponent({
    components: {
        IonContent,
        IonPage,
        IonSelectOption,
        IonList,
        IonToolbar,
        IonHeader,
        IonTitle,
        IonButtons,
        IonItem,
        IonLabel,
        IonSelect,
        IonButton,
        IonInput
      },
      setup() {
      const router = useRouter();
      const data = ref ({
        tipologia: "",
        razza: "",
        colore: "",
        taglia: "",
        anni: 0,
        vaccinato: "",
        regione:"",
        citta:"",
        descrizione:"",
        nome_animale:"",
        file:null
      }); //informazioni sull'annuncio da pubblicare
      
    //riduce la qualità dell'immagine  
    const handleChange = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();
          
    reader.onload = (event) => {

      const img = new Image();
      img.onload = () => {
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = img.width / 2; // Imposta la larghezza della nuova immagine
        canvas.height = img.height / 2; // Imposta l'altezza della nuova immagine
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
        canvas.toBlob((blob) => {
          data.value.file = new File([blob], file.name, { type: file.type });
        }, file.type, 0.5);
      };
      img.src = event.target.result;
    };

  reader.readAsDataURL(file);
};
 
    const showLoading = async () => {
            const loading = await loadingController.create({
              message: 'Caricamento...',
              duration: 4000
            });
            
            loading.present();
          }

      const profile = () =>{router.push("/profile")}
      //controlla se l'annuncio rispetta i parametri richiesti, in caso positivo invia la richiesta al back
      const publish=()=> {
        if (data.value.nome_animale === "" || data.value.tipologia === "" || data.value.razza === "" || data.value.colore === ""|| data.value.taglia === ""  || data.value.vaccinato === "" || data.value.regione === "" || data.value.citta === "" || data.value.descrizione === "" || data.value.file==null) 
        {
            alert("Errore: Compila tutti i campi");
            return;
        }
        if(isValidFormat(data.value.citta)||isValidFormat(data.value.nome_animale)||isValidFormat(data.value.razza))
        {
          alert("Errore: I campi città, nome e razza non possono contenere caratteri speciali");
          return;
        }


        if(data.value.citta.length>20 || data.value.razza.length>20 ||data.value.nome_animale.length>20 || data.value.descrizione.length>100)
        {
          alert("Errore: I campi razza, città e nome non devono superare i 20 caratteri mentre il campo descrizione massimo 100 caratteri")
          return;
        }
        if(data.value.citta.length<2||data.value.razza.length<2||data.value.nome_animale.length<2 || data.value.descrizione.length<20)
        {
          alert("Errore: I campi razza, città e nome devono contenere minimo 2 caratteri mentre il campo descrizione minimo 20 caratteri")
          return;
        }

        if(data.value.file.size > 2*1024*1024) //massima dimensione upload
        {
          alert("Errore: La dimensione massima consentita per le foto è di 4MB")
          return;
        }

        data.value.anni=Number(data.value.anni)
        if(isNaN(data.value.anni)||data.value.anni <0)
        {
            alert("Errore: Inserisci un numero valido");
            return;
        }

        //converto le info in formData così da poter inviare anche la foto salvata in base64
        const formData = new FormData();
        formData.append("tipologia", data.value.tipologia);
        formData.append("razza", data.value.razza);
        formData.append("colore", data.value.colore);
        formData.append("taglia", data.value.taglia);
        formData.append("anni", data.value.anni);
        formData.append("vaccinato", data.value.vaccinato);
        formData.append("regione", data.value.regione);
        formData.append("citta", data.value.citta);
        formData.append("descrizione", data.value.descrizione);
        formData.append("nome_animale", data.value.nome_animale);
        formData.append("file", data.value.file); 
        showLoading()
        axios.post('http://127.0.0.1:5000/publishPost',formData,{
              headers: {
                "Content-Type": "multipart/form-data",
                "Authorization": localStorage.getItem("token")
              }
          }
          
          )
        .then( response=> {
          if(response.status==200)
          {//NON FUNZIONA PER MOBILE
            
            Notification.requestPermission()
            .then(permission => {
              if (permission === 'granted') {
                new Notification('Animaletto', {
                  body: 'Post pubblicato con successo!'
                });
          }
        });
            router.push("/profile")
            localStorage.setItem("refresh",1) //refresh del profilo
          }
        })
        .catch(() => {
          alert("errore")
          
        })
      }
      function isValidFormat(stringa) 
      {
        return /[^\w\s]/gi.test(stringa);
      }

      return{data,profile,publish,handleChange}
    }
  });
  
  </script>
  
  <style scoped>
  ion-content {
    --background: url(../wall.jpg) 100% 100% no-repeat;
  }


</style>