import Vue from 'vue'
import Router from 'vue-router'
import Recipe from '@/views/Recipe.vue'
import Home from '@/views/Home.vue'
import Info from "@/views/Info.vue"
import Highscore from "@/views/Highscore";
import GetRandomRecipe from "@/views/RandomRecipe";

import firebase from 'firebase'
import qs from 'qs';
import Login from "@/components/dashboard/Login";
import Dashboard from "@/components/dashboard/Dashboard";


Vue.use(Router);

/*
IF LOGIN IS REQUIRED FOR THE VIEW ADD:
meta: {
        requiresAuth: true
      }
*/

const router = new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/recipe/:id',
            name: 'specific-recipe',
            component: Recipe,
        },
        {
            path: '/recipe',
            name: 'random-recipe',
            component: GetRandomRecipe
        },
        {
            path: "/info",
            name: "info",
            component: Info
        },
        {
            path: "/highscore",
            name: "highscore",
            component: Highscore
        },
        {
            path: "/login",
            name: "login",
            component: Login
        },
        {
            path: "/dashboard",
            name: "dashboard",
            component: Dashboard
        },
        {
            path: "*",
            redirect: "/"
        }
    ],
    parseQuery(query) {
        return qs.parse(query);
    },
    stringifyQuery(query) {
        var result = qs.stringify(query);

        return result ? ('?' + result) : '';
    }
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