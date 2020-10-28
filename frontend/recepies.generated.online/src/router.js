import Vue from 'vue'
import Router from 'vue-router'
import Recipe from './views/Recipe.vue'
import Info from "./views/Info.vue"

import firebase from 'firebase'

Vue.use(Router);

/*
IF LOGIN IS REQUIRED FOR THE VIEW ADD:
meta: {
        requiresAuth: true
      }
*/

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/recipe/:id',
      name: 'recipe2',
      component: Recipe
    },
    {
      path: '/',
      name: 'recipe',
      component: Recipe
    },
    {
      path: "/info",
      name: "info",
      component: Info
    }
  ]
});

router.beforeEach((to, from, next) => {
  let verified = false;
  let validated = false;

  if (firebase.auth().currentUser) {
    verified = firebase.auth().currentUser.emailVerified;
    validated = true
  }

  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);

  if (requiresAuth && !verified) next('login');
  else if (requiresAuth && validated && !verified) next('verify');
  else if (verified && ((to.path === '/signup') || (to.path === '/login') || (to.path === '/verify'))) next('dashboard');
  else if (!validated && ((to.path === '/verify'))) next('login');
  else next()
});

export default router
