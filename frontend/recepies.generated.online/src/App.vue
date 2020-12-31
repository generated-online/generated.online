<template>
    <v-app id="inspire" :style="cssVars">
        <v-main>
            <EmojieBackground :class="{'background-animation': addBackgroundID}"
                              :color="backgroundColor" :opacity="1"
                              :recipe="recipe"
                              class="background prev-color"/>
            <v-container>
                <router-view :key="$route.fullPath" @recipe="updateRecipe($event)"
                             @shareText="updateTitle($event)">
                </router-view>
            </v-container>
            <!-- it looks like this fucks up refinement-->
            <v-btn
                    v-show="showScrollUpButton"
                    v-scroll="onScroll"
                    :right="$vuetify.breakpoint.mdAndUp"
                    :style="($vuetify.breakpoint.smAndDown?'left: 50%; transform: translateX(-50%)':'')"
                    bottom
                    class="boldyAppearing"
                    dark
                    fab
                    fixed
                    @click="toTop"
            >
                <v-icon>keyboard_arrow_up</v-icon>
            </v-btn>
        </v-main>
        <Footer :addBackgroundID="addBackgroundID" :recipeId="recipeID" :shareText="shareText"/>
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
            scrolledToBottom: false,
            showScrollUpButton: false
        };
    },
    methods: {
        updateTitle(shareText) {
            this.shareText = shareText;
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
        onScroll(e) {
            if (typeof window === 'undefined') return
            const top = window.pageYOffset || e.target.scrollTop || 0
            this.showScrollUpButton = top > 20
            let scrolledToBottom = Math.max(window.pageYOffset, document.documentElement.scrollTop, document.body.scrollTop) + window.innerHeight >= document.documentElement.offsetHeight - 20

            if (scrolledToBottom !== this.scrolledToBottom) {
                this.scrolledToBottom = scrolledToBottom
                this.$store.commit("setScroll", this.scrolledToBottom)
            }
        },
        toTop() {
            this.$vuetify.goTo(0)
        },
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
                "red": "rgb(231, 55, 61)"
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

.bg-black {
  background-color: rgb(0, 0, 0);
}

.boldyAppearing {
  background: black;
  padding: 20px !important;
  border-radius: 30px !important;
  color: var(--bg-color) !important;
  animation: fade-in 1s forwards;
  -webkit-animation: fade-in 1s forwards;
  opacity: 0;
}

.boldy {
  background: black;
  padding: 20px !important;
  border-radius: 30px !important;
  color: var(--bg-color) !important;
}

.boldyNoColor {
  background: black;
  padding: 20px !important;
  border-radius: 30px !important;
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

.noBoxShadow {
  box-shadow: none !important;
}
.small-emoji {
  vertical-align: middle;
  height: 1em;
}
</style>