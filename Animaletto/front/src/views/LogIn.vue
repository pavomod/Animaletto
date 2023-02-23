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
import { IonItem, IonLabel, IonInput, IonButton } from "@ionic/vue";


export default defineComponent({
  name: 'LoginPage',
  components: {
      IonItem,
      IonLabel,
      IonInput,
      IonButton,
    },
  setup() {

    const data = ref ({
      username: "",
      password: "",
      error: ""
    });
    const goToSignUp = () => {
      window.location.href = '/signup'
      };
    const login = () => {
      if (data.value.username === "" || data.value.password === "") {
        alert("Errore: stringhe vuote.");
        return;
      }
      axios.post('http://192.168.248.104:5000/login', { 
        username: data.value.username, 
        password: data.value.password 
      },{
            headers: {
              "Content-Type": "multipart/form-data",
            }
        }

      )
      .then(async (response) => {
        localStorage.setItem('token', response.data.token);
        window.location.href = '/profile'
      })
      .catch(error => {
        
        alert("errore backend: "+error)
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