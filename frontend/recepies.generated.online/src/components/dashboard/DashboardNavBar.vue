<template>
        <v-app-bar
                dark
        >
            <v-toolbar-title> Dashboard </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-spacer v-if="user.loggedIn">Hello {{this.user.data.email}}</v-spacer>
            <v-btn v-if="user.loggedIn" icon @click.prevent="signOut">
                <v-icon>logout</v-icon>
            </v-btn>
            <v-btn v-else icon to="login">
                <v-icon>login</v-icon>
            </v-btn>
        </v-app-bar>
</template>
<script>
import {mapGetters} from "vuex";
import firebase from "firebase";

export default {
    computed: {
        ...mapGetters({
// map `this.user` to `this.$store.getters.user`
            user: "user"
        })
    },
    methods: {
        signOut() {
            firebase
                .auth()
                .signOut()
                .then(() => {
                    this.$router.replace({
                        name: "login"
                    });
                });
        }
    }
};
</script>