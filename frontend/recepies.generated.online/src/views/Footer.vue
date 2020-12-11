<template>
    <v-footer padless fixed style="background: transparent">
        <v-card flat tile width="100%" class="footer-container text-center" style="background: transparent">
            <v-card-text class="py-2 px-0 text center" width="100%">
                <v-btn class="mx-3 my-0 boldy remove-acive" to="/" icon>
                    <v-icon class="vue-icon" size="30">search</v-icon>
                </v-btn>

                <v-btn to="/recipe" icon class="mx-3 my-0 boldy">
                    <v-icon class="vue-icon">shuffle</v-icon>
                </v-btn>

                <v-btn class="mx-3 my-0 boldy" icon to="/info">
                    <v-icon class="vue-icon" size="30">mdi-information-outline</v-icon>
                </v-btn>

                <v-btn class="mx-3 my-0 boldy" icon>
                    <!-- show whatsapp share button, when not loaded yet just an empty button -->
                    <ShareNetwork class="inline-block" network="whatsapp" style="text-decoration: unset" :url="url"
                        :title="shareText">
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

<style scoped lang="scss">
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
</style>