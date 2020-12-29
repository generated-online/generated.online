import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// vue dev plugin
Vue.config.devtools = process.env.NODE_ENV === 'development'

export default new Vuex.Store({
    state: {
        scrolledToBottom: false,
        user: {
            loggedIn: false,
            data: null
        }
    },
    getters: {
        user(state){
            return state.user
        }
    },
    mutations: {
        setScroll(state, payload){
            state.scrolledToBottom = payload
        },
        SET_LOGGED_IN(state, value) {
            state.user.loggedIn = value;
        },
        SET_USER(state, data) {
            state.user.data = data;
        }
    },
    actions: {
        fetchUser({ commit }, user) {
            commit("SET_LOGGED_IN", user !== null);
            if (user) {
                commit("SET_USER", {
                    displayName: user.displayName,
                    email: user.email
                });
            } else {
                commit("SET_USER", null);
            }
        }
    }
})