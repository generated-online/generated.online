<template>
    <v-app id="inspire" :style="cssVars">
        <v-main >
            <EmojieBackground :recipe="recipe" :opacity="1" :color="backgroundColor"/>
            <v-container>
                <router-view :key="$route.path" @shareText="updateTitle($event)" @recipe="updateRecipe($event)">
                </router-view>
            </v-container>
        </v-main>
        <Footer :shareText="shareText" :recipeId="recipeID"/>
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
                "background-color": "transparent"
            }
        }
    }

}
</script>

<style lang="scss">
$softPink: var(--bg-color);


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
  // background: rgba(255, 255, 255, 0.05);
  text-shadow: 0px 0px 20px $softPink;
}

.black-button {
  background: rgba(1, 1, 1, 0.8) !important;
  color: white !important;
  box-shadow: unset !important;
}
</style>