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
import { IonItem, IonLabel, IonInput, IonButton } from "@ionic/vue";


export default defineComponent({
  name: 'SignupPage',
  components: {
      IonItem,
      IonLabel,
      IonInput,
      IonButton,
    },
    setup() {

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
    const goToLogin = () =>{window.location.href = '/auth'}
    const registerUser=()=> {
      if (data.value.username === "" || data.value.password === "" || data.value.nome === ""|| data.value.cognome === "" || data.value.confirmPassword === "" || data.value.email === "" || data.value.cellulare === "") 
      {
        alert("Errore: stringhe vuote.");
        return;
      }
      if(data.value.password != data.value.confirmPassword)
      {
        alert("Errore: le password non sono uguali");
        return;
      }
      if(data.value.cellulare.length>12)
      {
        alert("Inserisci un numero valido")
        return;
      }
        data.value.cellulare=Number(data.value.cellulare)
        if(isNaN(data.value.cellulare))
        {
          alert("Inserisci un numero valido");
          return;
        }

        if(!data.value.email.includes("@") ||!data.value.email.includes(".")) 
        {
          alert("Email non valida");
          return;
        }

      axios.post('http://192.168.248.104:5000/signin', {
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
      .then( ()=> {
        window.location.href = '/auth'
      })
      .catch(() => {
        alert("errore backend")
        
      })
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