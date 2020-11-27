<template>
    <div id="app">
        <v-app id="inspire" :style="cssVars">
            <router-view :key="$route.path" @shareText="updateTitle($event)" @recipeId="updateRecipeId($event)">
            </router-view>
            <Footer :shareText="shareText" :recipeId="recipeId" />
        </v-app>
    </div>
</template>

<script>
    import Footer from "./views/Footer";
    import recipeToColor from "@/functions/recipe_to_color";

    export default {
        components: {
            Footer
        },
        methods: {
            updateTitle(shareText) {
                this.shareText = shareText;
                this.$analytics.logEvent("notification_received");
            },
            updateRecipeId(id) {
                this.recipeId = id;
                this.backgroundColor = recipeToColor(this.recipeId);
            }
        },
        data() {
            return {
                url: "",
                shareText: "Schau dir diese coolen von einer KI generierten Rezepte an!",
                recipeId: null,
                backgroundPosition: (window.innerWidth % 90) / 2 + "px",
                backgroundColor: recipeToColor(null)
            };

        },
        created() {
            this.url = window.location.href;
        },
        mounted() {
            window.addEventListener('resize', () => {
                this.backgroundPosition = (window.innerWidth % 90) / 2 + "px";
            })
        },
        computed: {
            cssVars() {
                return {
                    '--bg-color': this.backgroundColor,
                }
            }
        }

    }
</script>

<style lang="scss">
    $softPink: var(--bg-color);

    #inspire {
        background-color: transparent;
    }


    #app {
        margin: 0;
        padding: 0;
        overflow-x: hidden;
        max-width: 100vw !important;
        min-height: 100vh !important;
        font-family: "Roboto";
    }

    .text-span {
        // background: $softPink;
        background: rgba(0, 0, 0, 0.05);
        text-shadow: 0px 0px 20px $softPink;
    }
</style>