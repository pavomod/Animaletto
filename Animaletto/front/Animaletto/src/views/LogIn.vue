<template>
  <ion-page>
    <ion-header>
      <ion-toolbar color="primary">
        <ion-title>Login</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding">
        <ion-item>
          <ion-label position="floating"><b>Username</b></ion-label>
          <ion-input v-model="data.username"></ion-input>
        </ion-item>
        
        <ion-item>
          <ion-label position="floating"><b>Password</b></ion-label>
          <ion-input type="password" v-model="data.password"></ion-input>
        </ion-item>
        <br>
        <ion-button expand="block" @click="login">Login</ion-button>
        <div id="signUpBlock" class="ion-text-center ion-margin-top">
          <p style="color:white"><b>Non hai un account?</b></p>
        </div>
        <ion-button expand="block" @click="goToSignUp">Registrati</ion-button>
  
    </ion-content>
    
  </ion-page>
</template>
  
<script>
import axios from 'axios'
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";
import { IonPage,IonContent,IonHeader,IonToolbar,IonTitle,IonItem, IonLabel, IonInput, IonButton } from "@ionic/vue";


export default defineComponent({
  name: 'LoginPage',
  components: {
      IonPage,
      IonContent,
      IonHeader,
      IonToolbar,
      IonTitle,
      IonItem,
      IonLabel,
      IonInput,
      IonButton,
    },
  setup() {
 //NON FUNZIONA PER MOBILE
 
    Notification.requestPermission()
         .then(permission => {
          if (permission === 'granted') {
            new Notification('Animaletto', {
              body: 'Benvenuto su animaletto!'
            });
          }
        });
   
    const router = useRouter();
    const data = ref ({
      username: "",
      password: "",
      error: ""
    });
    const goToSignUp = () => {
      router.push("/signup");
      };
    const login = () => {
      if (data.value.username === "" || data.value.password === "") {
        alert("Errore: Inserisci dei valori.");
        return;
      }
      axios.post('http://127.0.0.1:5000/login', { 
        username: data.value.username, 
        password: data.value.password 
      },{
            headers: {
              "Content-Type": "multipart/form-data",
            }
        }

      )
      .then(response => {
        if(response.status==200)
        {
          localStorage.setItem("refresh", "1"); //richiedo il refresh della pagina
          localStorage.setItem('token', response.data.token); //salvataggio del token ricevuto dal back
          router.push("/profile")          
        }
      })
      .catch(() => {
        alert("Credenziali errate")
      })
    }

    

    return { data, login,goToSignUp };
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