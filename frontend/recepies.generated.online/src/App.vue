<template>
    <div id="app">
        <v-app id="inspire">
            <router-view :key="$route.path" @shareText="updateTitle($event)"></router-view>
            <Footer :shareText="shareText" />
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
            }
        },
        data() {
            return {
                url: "",
                shareText: "Schau dir diese coolen von einer KI generierten Rezepte an!"
            };

        },
        created() {
            this.url = window.location.href;
        },
    }
</script>