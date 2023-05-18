<template>
  <ion-page>
    <ion-header>
      <ion-toolbar color="primary">
        <ion-title>Registrazione</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">
      <ion-item>
        <ion-label position="floating">Nome</ion-label>
        <ion-input  v-model="data.nome"></ion-input>
      </ion-item>
      <ion-item>
        <ion-label position="floating">Cognome</ion-label>
        <ion-input  v-model="data.cognome"></ion-input>
      </ion-item>
      <ion-item>
        <ion-label position="floating">email</ion-label>
        <ion-input type="email" v-model="data.email"></ion-input>
      </ion-item>
      <ion-item>
        <ion-label position="floating">cellulare</ion-label>
        <ion-input  v-model="data.cellulare"></ion-input>
      </ion-item>
      <ion-item>
        <ion-label position="floating">Username</ion-label>
        <ion-input  v-model="data.username"></ion-input>
      </ion-item>
      <ion-item>
        <ion-label position="floating">Password</ion-label>
        <ion-input type="password" v-model="data.password"></ion-input>
      </ion-item>
      <ion-item>
        <ion-label position="floating">Conferma Password</ion-label>
        <ion-input type="password" v-model="data.confirmPassword"></ion-input>
      </ion-item>
      <br><br>
      <ion-button expand="block" @click="registerUser">Registrati</ion-button>
      <div id="signUpBlock" class="ion-text-center ion-margin-top">
        <p style="color:white"><b>Vai al login</b></p>
      </div>
      
      <ion-button expand="block" @click="goToLogin">Login</ion-button>
      <br><br><br>
    </ion-content>
  </ion-page>
</template>

<script>
import axios from 'axios'
import { defineComponent, ref } from "vue";
import { IonPage,IonContent,IonItem, IonLabel, IonInput, IonButton,IonTitle,IonToolbar,IonHeader } from "@ionic/vue";
import { useRouter } from "vue-router";

export default defineComponent({
  name: 'SignupPage',
  components: {
      IonTitle,
      IonHeader,
      IonToolbar,
      IonItem,
      IonLabel,
      IonInput,
      IonButton,
      IonPage,
      IonContent
    },
    setup() {
    const router = useRouter();
    const data = ref ({
      nome: "",
      cognome: "",
      username: "",
      password: "",
      confirmPassword: "",
      error: "",
      email:"",
      cellulare:""
    });
    const goToLogin = () =>{router.push("/auth")}
    const registerUser=()=> {
      if (data.value.username === "" || data.value.password === "" || data.value.nome === ""|| data.value.cognome === "" || data.value.confirmPassword === "" || data.value.email === "" || data.value.cellulare === "") 
      {
        alert("Errore: stringhe vuote.");
        return;
      }
      if(isValidFormat(data.value.nome) ||isValidFormat(data.value.cognome))
      {
        alert("Errore: I campi nome e cognome non possono contenere caratteri speciali");
        return;
      }

      if(data.value.password != data.value.confirmPassword)
      {
        alert("Errore: le password non sono uguali");
        return;
      }
      if(data.value.password.length<8)
      {
        alert("Errore: la password deve essere lunga minimo 8");
        return;
      }
      if(data.value.cellulare.length>12||data.value.cellulare.length<4)
      {
        alert("Il campo cellulare deve essere lungo minimo 4 e massimo 12")
        return;
      }
        data.value.cellulare=Number(data.value.cellulare) //verifica che i dati inseriti siano effettivamente numerici
        if(isNaN(data.value.cellulare))
        {
          alert("Inserisci un numero valido");
          return;
        }

        if(!isValidEmail(data.value.email)) //tramite regex verifica la sintassi dell'email
        {
          alert("Email non valida");
          return;
        }
        if(data.value.nome.length<2||data.value.cognome.length<2||data.value.username.length<2)
        {
          alert("Errore: I campi nome, cognome e username devono contenere minimo 2 caratteri")
          return;
        }

      axios.post('http://127.0.0.1:5000/signin', {
        nome: data.value.nome,
        cognome: data.value.cognome,
        username: data.value.username,
        password: data.value.password,
        email: data.value.email,
        cellulare: data.value.cellulare,
      },{
            headers: {
              "Content-Type": "multipart/form-data",
            }
        })
      .then( response=> {
        if(response.status==200)
        {//NON FUNZIONA PER MOBILE
          
          Notification.requestPermission()
         .then(permission => {
          if (permission === 'granted') {
            new Notification('Animaletto', {
              body: 'Utente registrato con successo!'
            });
          }
        });
         router.push("/auth")
        
        }
      })
      .catch(() => {
        alert("Utente già registrato o errore nel contattare il server.")
        
      })
    }
    function isValidEmail(email) 
    {
      // Definizione della RegEx per controllare l'email
      const emailPattern = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,})+$/;
      // Utilizzo della RegEx per validare l'email
      return emailPattern.test(email);
    }
    function isValidFormat(stringa) 
    {
      return /[^\w\s]/gi.test(stringa);
    }

    return{data,registerUser,goToLogin}
  }
});

</script>

<style scoped>
  ion-content {
    --background: url(../wall.jpg) 100% 100% no-repeat;
  }

  ion-item {
    --background: transparent !important;
    --color: #fff !important;
    --placeholder-color: #fff !important;
  }
</style>