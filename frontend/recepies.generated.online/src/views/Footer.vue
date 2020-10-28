<template>
    <v-card>
        <v-footer padless fixed>
            <v-card flat tile width="100%" class="footer-container lighten-1 text-center">
                <v-card-text class="py-2 text center" width="100%">
                    <span class="mx-4 mr-0">
                        neues rezept
                    </span>
                    <v-btn class="mx-4 ml-0" icon>
                        <router-link to="/recipe">
                            <img src="/reload.svg" class="my-icon" />
                        </router-link>
                    </v-btn>
                    <v-btn class="mx-4 my-0" icon>
                        <a href="https://github.com/generated-online/generated.online" class="inline-block">

                            <img src="/github.png" class="my-icon" />
                        </a>
                    </v-btn>
                    <v-btn class="mx-4 my-0" icon>
                        <router-link to="/info">
                            <img src="/info.svg" class="my-icon" />
                        </router-link>
                    </v-btn>
                    <v-btn class="mx-4 my-0" icon>
                        <!-- show whatsapp share button, when not loaded yet just an empty button -->
                        <ShareNetwork class="inline-block" network="whatsapp" :url="url" :title="shareText">
                            <img src="/whatsapp.svg" class="my-icon" />
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
    Vue.use(VueSocialSharing);

    export default {
        name: "big-footer",
        props: {
            "shareText": {
                type: String,
                default: "Schau dir diese coolen von einer KI generierten Rezepte an!"
            }
        },
        components: {
            VueSocialSharing
        },
        data() {
            return {
                url: "",
            };
        },
        watch: {
            '$route': function (refreshPage) {
                this.url = window.location.href;
            }
        }
    }
</script>

<style>
    .footer-container {
        background-color: rgb(93, 146, 177) !important;
        color: white !important;
    }

    .my-icon {
        cursor: grab;
        filter: invert(77%) sepia(90%) saturate(1%) hue-rotate(10deg) brightness(88%) contrast(108%);
        opacity: 0.8;
        width: 1.75em;
        height: 1.75em;
    }

    .footer-text {
        color: rgb(211, 211, 211);
    }
</style>