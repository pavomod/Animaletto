import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import MyProfile from '../views/MyProfile.vue'
import LogIn from '../views/LogIn.vue'
import SignUp from '../views/SignUp.vue'
import DashBoard from '../views/DashBoard.vue'
import NewPost from '../views/NewPost.vue'
const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/profile'
  },
  {
    path: '/Profile',
    name: 'Profile',
    component: MyProfile
  },  
  {
    path: '/auth',
    name: 'Auth',
    component: LogIn
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/dashBoard',
    name: 'DashBoard',
    component: DashBoard
  },
  {
    path: '/newPost',
    name: 'NewPost',
    component: NewPost
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
