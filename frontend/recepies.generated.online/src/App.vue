<template>
    <v-app id="inspire" :style="cssVars">
        <v-main>
            <EmojieBackground :recipe="recipe" :opacity="1" :color="backgroundColor" />
            <v-container>
                <router-view :key="$route.path" @shareText="updateTitle($event)" @recipe="updateRecipe($event)">
                </router-view>
            </v-container>
        </v-main>
        <Footer :shareText="shareText" :recipeId="recipeID" />
    </v-app>
</template>

<script>
    import Footer from "./views/Footer";
    import recipeToColor from "@/functions/recipe_to_color";
    import EmojieBackground from "@/components/EmojieBackground";

    export default {
        components: {
            Footer,
            EmojieBackground
        },
        methods: {
            updateTitle(shareText) {
                this.shareText = shareText;
                this.$analytics.logEvent("notification_received");
            },
            updateRecipe(recipe) {
                this.recipe = recipe;
                if (!recipe) {
                    this.recipeID = null
                } else {
                    this.recipeID = recipe.id
                }
                this.backgroundColor = recipeToColor(this.recipeID);
            }
        },
        data() {
            return {
                url: "",
                shareText: "Schau dir diese coolen von einer KI generierten Rezepte an!",
                recipe: null,
                recipeID: null,
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
                    "background-color": "transparent",
                    "green": "rgb(195, 211, 91)",
                }
            }
        }

    }
</script>

<style lang="scss">
    $softPink: var(--bg-color);

    .bg-green {
        background: rgb(195, 211, 91);
    }

    .boldy-red {
        color: black !important;
        background: rgb(231, 55, 61) !important;
        padding: 20px !important;
        border-radius: 30px !important;
    }

    .boldy-color {
        color: black !important;
        background: var(--bg-color) !important;
        padding: 20px !important;
        border-radius: 30px !important;
    }

    .boldy-border {
        border: 2px solid var(--bg-color) !important;
        ;
        border-radius: 15px;
        padding: 10px
    }

    .boldy {
        background: black;
        padding: 20px !important;
        border-radius: 30px !important;
        color: var(--bg-color) !important;
    }

    .ais-SearchBox-input::placeholder {
        color: var(--bg-color) !important;

    }

    #app {
        margin: 0;
        padding: 0;
        overflow-x: hidden;
        max-width: 100vw !important;
        min-height: 100vh !important;
        font-family: "Roboto";
    }

    .info-container {
        background-color: rgba(0, 0, 0, 0) !important;
        border: none !important;
        box-shadow: none !important;
    }

    .black-button {
        background: rgba(1, 1, 1, 0.8) !important;
        color: white !important;
        box-shadow: unset !important;
    }


    .v-divider {
        border-color: rgba(0, 0, 0, 0.3) !important;
    }

    .shady {
        border-radius: 5px;
        box-shadow: 0 0 10px black;
        background: rgba(0, 0, 0, 0.8);
        color: white;
    }
</style>