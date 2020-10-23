import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import '@babel/polyfill'
import firebase from "firebase";


const firebaseConfig = {
  apiKey: "AIzaSyDmmSPNA_lC7rtpuS3-Yx4dmy4BegppYIw",
  authDomain: "generatedonline-a1cb0.firebaseapp.com",
  databaseURL: "https://generatedonline-a1cb0.firebaseio.com",
  projectId: "generatedonline-a1cb0",
  storageBucket: "generatedonline-a1cb0.appspot.com",
  messagingSenderId: "988309438314",
  appId: "1:988309438314:web:0db27d9fa52f9108172f13"
};

firebase.initializeApp(firebaseConfig);
Vue.config.productionTip = false

firebase.auth().onAuthStateChanged(() => {
  new Vue({
    router,
    store,
    render: h => h(App)
  }).$mount('#app')
})
