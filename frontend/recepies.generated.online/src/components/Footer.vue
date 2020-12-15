<template>
    <v-footer fixed padless style="background: transparent; pointer-events: none;">
        <v-card class="footer-container text-center" flat style="background: transparent" tile width="100%">
            <v-card-text :style="{'margin-right': $vuetify.breakpoint.smAndDown? '0.3em':'auto',
            'width': $vuetify.breakpoint.smAndDown? 'min-content':'max-content'}"
                         class="py-1 px-0 text center allIcons" :class="{'background-animation': addBackgroundID}">
                <v-btn class="mx-2 my-1 boldy remove-acive" icon to="/">
                    <v-icon class="vue-icon" size="30">search</v-icon>
                </v-btn>

                <v-btn class="mx-1 my-1 boldy" icon to="/recipe">
                    <v-icon class="vue-icon">shuffle</v-icon>
                </v-btn>

                <v-btn class="mx-1 my-1 boldy" icon to="/highscore">
                    <img src="../assets/robokoch.png" class="color-adapt vue-icon">
                </v-btn>
                <v-btn class="mx-2 my-1 boldy" icon to="/info">
                    <v-icon class="vue-icon" size="30">mdi-information-outline</v-icon>
                </v-btn>

                <v-btn class="mx-2 my-1 boldy" icon>
                    <!-- show whatsapp share button, when not loaded yet just an empty button -->
                    <ShareNetwork :title="shareText" :url="url" class="inline-block" network="whatsapp"
                                  style="text-decoration: unset">
                        <v-icon class="vue-icon" size="30">mdi-whatsapp</v-icon>
                    </ShareNetwork>
                </v-btn>
            </v-card-text>
        </v-card>
    </v-footer>
</template>

<script>
import Vue from "vue";
import VueSocialSharing from "vue-social-sharing";
import recipeToColor from "@/functions/recipe_to_color";
import generateRecipeButton from "@/components/generateRecipeButton";
import {getImgUrl} from "@/functions/emojiUtils"

Vue.use(VueSocialSharing);

export default {
    name: "big-footer",
    props: {
        shareText: {
            type: String,
            default: "Schau dir diese coolen von einer KI generierten Rezepte an!"
        },
        recipeId: {
            type: String,
            default: null
        },
        addBackgroundID: {
            trype: Boolean,
            default: false
        }
    },
    components: {
        VueSocialSharing,
        generateRecipeButton
    },
    data() {
        return {
            url: window.location.href,
            color: recipeToColor(this.recipeId),
        };
    },
    watch: {
        '$route': function () {
            this.url = window.location.href;
        },
        'recipeId': function () {
            this.color = recipeToColor(this.recipeId);
        }
    },
    methods: {
        getImgUrl,
    }
}
</script>

<style lang="scss" scoped>
.v-btn:not(.v-btn--text):not(.v-btn--outlined).v-btn--active:before {
  opacity: 0 !important;
}

a:link {
  color: var(--bg-color)
}

.footer-container {
  color: white !important;
}

.vue-icon {
  cursor: grab;
  //color: transparent;
  //text-shadow: 0 0 0 var(--bg-color);
  height: 1.5em;
}

.allIcons {
  margin-left: auto;
  background: var(--prev-bg-color);
  border-radius: 35px !important;
  pointer-events: all;
  margin-bottom: 0.3em;
  height: max-content;
}
</style>