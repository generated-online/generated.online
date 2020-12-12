<template>
    <v-card class="info-container py-4 px-2 mt-16 mb-8">
        <div class="text-sm-h2 text-md-h1 text-h4 pb-12 mb-16 text-center">
            <b class="boldy" style="font-size:6vw">KI generierte Rezepte!</b>
        </div>
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
