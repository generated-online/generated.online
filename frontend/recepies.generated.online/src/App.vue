<template>
    <div id="app">
        <v-app id="inspire">
            <router-view :key="$route.path" @shareText="updateTitle($event)" @recipeId="updateRecipeId($event)"></router-view>
            <Footer :shareText="shareText" :recipeId="recipeId" />
        </v-app>
    </div>
</template>

<script>
    import Footer from "./views/Footer";
    export default {
        components: {
            Footer
        },
        methods: {
            updateTitle(shareText) {
                this.shareText = shareText;
            },
            updateRecipeId(id){
                this.recipeId = id;
            }
        },
        data() {
            return {
                url: "",
                shareText: "Schau dir diese coolen von einer KI generierten Rezepte an!",
                recipeId: null
            };

        },
        created() {
            this.url = window.location.href;
        },
    }
</script>

<style>
    body,
    #app {
        margin: 0;
        padding: 0;
        overflow-x: hidden;
        max-width: 100vw !important;
        min-height: 100vh !important;
        font-family: "Roboto";
    }
</style>