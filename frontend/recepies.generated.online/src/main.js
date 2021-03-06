import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from '@/plugins/vuetify'

import '@babel/polyfill'
import * as firebase from "firebase/app";
import "firebase/firestore";
import "firebase/analytics";

import InstantSearch from 'vue-instantsearch'

Vue.use(InstantSearch)

import VueCookies from 'vue-cookies'

Vue.use(VueCookies)
Vue.$cookies.config('1y')

const firebaseConfig = {
    apiKey: "AIzaSyDmmSPNA_lC7rtpuS3-Yx4dmy4BegppYIw",
    authDomain: "generatedonline-a1cb0.firebaseapp.com",
    databaseURL: "https://generatedonline-a1cb0.firebaseio.com",
    projectId: "generatedonline-a1cb0",
    storageBucket: "generatedonline-a1cb0.appspot.com",
    messagingSenderId: "988309438314",
    appId: "1:988309438314:web:0db27d9fa52f9108172f13",
    measurementId: "G-P84D64G1BB"
};

firebase.default.initializeApp(firebaseConfig);
firebase.default.analytics();

Vue.config.productionTip = false;

Vue.prototype.$analytics = firebase.default.analytics();

// vue dev plugin
Vue.config.devtools = process.env.NODE_ENV === 'development'

let app
firebase.default.auth().onAuthStateChanged((user) => {
    if (!app) {
        app = new Vue({
            router,
            store,
            render: h => h(App),
            vuetify
        }).$mount('#app')
    }
    if (user){
        store.dispatch("fetchUser", user);
    }
})

// vue dev plugin
window.__VUE_DEVTOOLS_GLOBAL_HOOK__.Vue = app.constructor