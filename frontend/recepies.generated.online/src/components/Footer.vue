<template>
    <v-footer fixed padless style="background: transparent">
        <v-card class="footer-container text-center" flat style="background: transparent" tile width="100%">
            <v-card-text :style="{'margin-right': $vuetify.breakpoint.smAndDown? '0':'auto',
            'width': $vuetify.breakpoint.smAndDown? 'min-content':'max-content'}"
                         class="py-2 px-0 text center allIcons">
                <v-btn class="mx-2 my-1 boldy remove-acive" icon to="/">
                    <v-icon class="vue-icon" size="30">search</v-icon>
                </v-btn>

                <v-btn class="mx-1 my-1 boldy" icon to="/recipe">
                    <v-icon class="vue-icon">shuffle</v-icon>
                </v-btn>

                <v-btn class="mx-1 my-1 boldy" icon to="/highscore">
                    <span class="vue-icon">👩‍🍳</span>
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

Vue.use(VueSocialSharing);

export default {
    name: "big-footer",
    props: {
        "shareText": {
            type: String,
            default: "Schau dir diese coolen von einer KI generierten Rezepte an!"
        },
        "recipeId": {
            type: String,
            default: null
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
}

.footer-text {
  color: rgb(211, 211, 211);
}

.allIcons {
  margin-left: auto;
  background: var(--bg-color);
  border-radius: 35px !important;
}
</style>