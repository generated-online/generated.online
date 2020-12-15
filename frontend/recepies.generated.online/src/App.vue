<template>
    <v-app id="inspire" :style="cssVars">
        <v-main>
            <EmojieBackground :recipe="recipe" :opacity="1" :color="backgroundColor" class="background prev-color"
                :class="{'background-animation': addBackgroundID}" />
            <v-container>
                <router-view :key="$route.path" @shareText="updateTitle($event)" @recipe="updateRecipe($event)">
                </router-view>
            </v-container>
        </v-main>
        <Footer :shareText="shareText" :recipeId="recipeID" :addBackgroundID="addBackgroundID" />
    </v-app>
</template>

<script>
    import Footer from "./components/Footer";
    import recipeToColor from "@/functions/recipe_to_color";
    import EmojieBackground from "@/components/EmojieBackground";

    export default {
        components: {
            Footer,
            EmojieBackground
        },
        data() {
            return {
                url: "",
                shareText: "Schau dir diese coolen von einer KI generierten Rezepte an!",
                recipe: null,
                recipeID: null,
                backgroundPosition: (window.innerWidth % 90) / 2 + "px",
                backgroundColor: recipeToColor(null),
                prevBackgroundColor: recipeToColor(null),
                addBackgroundID: true,
            };
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
                this.prevBackgroundColor = String(this.backgroundColor);
                this.backgroundColor = recipeToColor(this.recipeID);
                // trigger animation
                this.addBackgroundID = false
                setTimeout(() => {
                    this.addBackgroundID = true
                }, 10)
            },
            nameToHSL(name) {
                let fakeDiv = document.createElement("div");
                fakeDiv.style.color = name;
                document.body.appendChild(fakeDiv);

                let cs = window.getComputedStyle(fakeDiv),
                    pv = cs.getPropertyValue("color");

                document.body.removeChild(fakeDiv);

                // Code ripped from RGBToHSL() (except pv is substringed)
                let rgb = pv.substr(4).split(")")[0].split(","),
                    r = rgb[0] / 255,
                    g = rgb[1] / 255,
                    b = rgb[2] / 255,
                    cmin = Math.min(r, g, b),
                    cmax = Math.max(r, g, b),
                    delta = cmax - cmin,
                    h = 0,
                    s = 0,
                    l = 0;

                if (delta == 0)
                    h = 0;
                else if (cmax == r)
                    h = ((g - b) / delta) % 6;
                else if (cmax == g)
                    h = (b - r) / delta + 2;
                else
                    h = (r - g) / delta + 4;

                h = Math.round(h * 60);

                if (h < 0)
                    h += 360;

                l = (cmax + cmin) / 2;
                s = delta == 0 ? 0 : delta / (1 - Math.abs(2 * l - 1));
                s = +(s * 100).toFixed(1);
                l = +(l * 100).toFixed(1);

                return h
            }
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
                    '--prev-bg-color': this.prevBackgroundColor,
                    "background-color": "transparent",
                    "green": "rgb(195, 211, 91)",
                    "--hue-filter": 'hue-rotate(' + (this.nameToHSL(this.backgroundColor) - 174) + 'deg)'
                }
            }
        }

    }
</script>

<style lang="scss">
    // https://stackoverflow.com/questions/1373142/preloading-css-images
    // css trick to preload loading image
    body::after {
        position: absolute;
        width: 0;
        height: 0;
        overflow: hidden;
        z-index: -1; // hide images
        content: url('/robokoch.gif'); // load images
    }

    @keyframes color-transition {
        from {
            background-color: var(--prev-bg-color);
        }

        to {
            background-color: var(--bg-color);
        }
    }

    .background-animation {
        animation: color-transition 2s forwards;
        -webkit-animation: color-transition 2s forwards;
        background-color: var(--prev-bg-color);
    }

    .prev-color {
        background-color: var(--prev-bg-color);

    }

    .now-color {
        background-color: var(--bg-color);

    }

    .background {
        pointer-events: none;
        position: absolute;
        top: 0em;
        right: 0;
        left: 0;
        overflow: hidden;
        bottom: 0px;
        -webkit-touch-callout: none;
        -webkit-user-select: none;
        -khtml-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        z-index: -1;
    }

    $softPink: var(--bg-color);

    @keyframes color-filter {
        0% {
            filter: hue-rotate(-174deg)
        }

        100% {
            filter: var(--hue-filter)
        }
    }

    .color-adapt {
        animation: color-filter 0.5s linear;
    }

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
        border-radius: 15px;
        padding: 10px
    }

    @keyframes fade-in {
        from {
            opacity: 0;
        }

        to {
            opacity: 1;
        }
    }

    .boldy {
        background: black;
        padding: 20px !important;
        border-radius: 30px !important;
        color: var(--bg-color) !important;
        animation: fade-in 1s forwards;
        -webkit-animation: fade-in 1s forwards;
        opacity: 0;
    }

    .boldyNoColor {
        background: black;
        padding: 20px !important;
        border-radius: 30px !important;
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

    .shady {
        border-radius: 5px;
        box-shadow: 0 0 10px black;
        background: rgba(0, 0, 0, 0.8);
        color: white;
    }
</style>