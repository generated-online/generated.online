<template>
    <v-card>
        <v-footer padless fixed>
            <v-card flat tile width="100%" class="footer-container lighten-1 text-center"
                :style="'background-color:' + color">
                <v-card-text class="py-2 px-0 text center" width="100%">
                    <v-btn class="mx-3 my-0" to="/" icon>
                        <v-icon class="vue-icon" size="30">search</v-icon>
                    </v-btn>
                    <generateRecipeButton buttonText="" />
                    <v-btn class="mx-3 my-0" icon to="/info">
                        <v-icon class="vue-icon" size="30">mdi-information-outline</v-icon>
                    </v-btn>
                    <v-btn class="mx-3 my-0" icon>
                        <!-- show whatsapp share button, when not loaded yet just an empty button -->
                        <ShareNetwork class="inline-block" network="whatsapp" style="text-decoration: unset" :url="url"
                            :title="shareText">
                            <v-icon class="vue-icon" size="30">mdi-whatsapp</v-icon>
                        </ShareNetwork>
                    </v-btn>
                </v-card-text>
            </v-card>
        </v-footer>
    </v-card>
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

<style>
    .footer-container {
        color: white !important;
    }

    .vue-icon {
        cursor: grab;
        color: rgba(0.82745098039, 0.82745098039, 0.82745098039, 0.6) !important;
    }

    .footer-text {
        color: rgb(211, 211, 211);
    }
</style>