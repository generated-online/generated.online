<template>
    <v-card class="info-container py-4 px-2 mt-16 mb-8">
        <v-card class="boldy text-sm-h2 text-md-h1 text-h4 mb-16 text-center ma-auto" style="background-color: black; width:fit-content "
                to="/">
            <b>
                <img alt="cooking robot" src="/robokoch.gif" style="vertical-align:middle; height: 8vw">
                Robo-Koch
                <img alt="cooking robot" src="/robokoch.gif" style="vertical-align:middle; height: 8vw">
            </b>
        </v-card>
        <div :style="searchWidth">
            <Search/>
        </div>
    </v-card>
</template>

<script>
import Search from "../components/Search";
import EmojieBackground from "@/components/EmojieBackground"

export default {
    name: "info",
    components: {
        Search,
        EmojieBackground
    },
    created() {
        this.$emit('shareText', "Schau dir diese coolen von einer KI generierten Rezepte an!");
        this.$emit('recipe', null);
    },
    computed: {
        searchWidth() {
            return {
                "width": this.$vuetify.breakpoint.xs ? '99%' : '80%',
                "margin": "auto"
            }
        }
    }
};
</script>