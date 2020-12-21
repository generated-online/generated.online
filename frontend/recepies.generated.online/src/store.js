import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// vue dev plugin
Vue.config.devtools = process.env.NODE_ENV === 'development'

export default new Vuex.Store({
    state: {
        scrolledToBottom: false
    },
    mutations: {
        setScroll(state, payload){
            state.scrolledToBottom = payload
        }
    },
    actions: {}
})
