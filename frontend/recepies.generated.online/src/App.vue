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
                    'border-left': this.backgroundPosition + ' solid',
                    'border-right': this.backgroundPosition + ' solid',
                    'padding-left': `calc(2em - ${this.backgroundPosition})`,
                    'padding-right': `calc(2em - ${this.backgroundPosition})`,
                }
            }
        }

    }
</script>

<style lang="scss">
    $softPink: var(--bg-color);
    $yellow: #F9A734;
    $DarkYellow: #FB8B24;
    $green: #36964C;
    $DarkGreen: #286E38;

    #inspire {
        // background:
        //     /* Pineapple details */
        //     radial-gradient(circle closest-side at 50px 50px, $DarkYellow 3px, transparent 0),
        //     radial-gradient(circle closest-side at 40px 60px, $DarkYellow 3px, transparent 0),
        //     radial-gradient(circle closest-side at 60px 60px, $DarkYellow 3px, transparent 0),
        //     radial-gradient(circle closest-side at 50px 70px, $DarkYellow 3px, transparent 0),

        //     radial-gradient(circle closest-side at 150px 165px, $DarkYellow 3px, transparent 0),
        //     radial-gradient(circle closest-side at 140px 175px, $DarkYellow 3px, transparent 0),
        //     radial-gradient(circle closest-side at 160px 175px, $DarkYellow 3px, transparent 0),
        //     radial-gradient(circle closest-side at 150px 185px, $DarkYellow 3px, transparent 0),

        //     /* Pineapple base */
        //     radial-gradient(ellipse closest-side at 50px 60px, $yellow 18px, transparent 0),

        //     radial-gradient(ellipse closest-side at 150px 175px, $yellow 18px, transparent 0),

        //     /* Pineapple leafs */
        //     radial-gradient(circle closest-side at 30px 40px, $softPink 15px, transparent 0),
        //     radial-gradient(circle closest-side at 40px 35px, $green 15px, transparent 0),
        //     radial-gradient(circle closest-side at 70px 40px, $softPink 15px, transparent 0),
        //     radial-gradient(circle closest-side at 60px 35px, $DarkGreen 15px, transparent 0),

        //     radial-gradient(circle closest-side at 130px 155px, $softPink 15px, transparent 0),
        //     radial-gradient(circle closest-side at 140px 150px, $green 15px, transparent 0),
        //     radial-gradient(circle at 170px 155px, $softPink 15px, transparent 0),
            // radial-gradient(circle at 160px 150px, $DarkGreen 15px, transparent 0);
        background-color: $softPink;
        background-size: 180px 210px;
        background-position: -15px 0;
        border-left-color: $softPink !important;
        border-right-color: $softPink !important;
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
        background: $softPink
    }
</style>