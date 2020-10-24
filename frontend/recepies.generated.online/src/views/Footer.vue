<template>
    <div class="footer-container">
        <div class="footer">
            <span class="footer-element">
                <router-link to="/" class="inline-block">
                    <img src="/reload.svg" class="icon" /></router-link>
            </span>
            <span class="vertical-line">
            </span>
            <span class="footer-element">
                <a href="https://github.com/generated-online/generated.online" class="inline-block">
                    <img src="/github.png" class="icon" /></a>
            </span>
            <span class="footer-element">
                <router-link to="/info"><img src="/info.svg" class="icon" /></router-link>
            </span>
            <!-- show whatsapp share button, when not loaded yet just an empty button -->
            <span class="footer-element" v-if="recipes.length !== 0">
                <ShareNetwork class="inline-block" network="whatsapp" :url="url"
                    :title="'Schau dir dieses coole Rezept an: ' + recipes[0]['title']">
                    <img src="/whatsapp.svg" class="icon" />
                </ShareNetwork>
            </span>
            <span class="footer-element inline-block" v-if="recipes.length === 0">
                <img src="/whatsapp.svg" class="icon" />
            </span>
        </div>
    </div>
</template>

<script>
    import Vue from "vue";
    import VueSocialSharing from "vue-social-sharing";
    Vue.use(VueSocialSharing);

    export default {
        name: "big-footer",
        props: {
            "recipes": {
                type: Array,
                default: function () {
                    return []
                }
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
        created() {
            this.url = window.location.href;
        },
    };
</script>

<style>
    body,
    #app {
        margin: 0;
        padding: 0;
        overflow-x: hidden;
        max-width: 100vw !important;
        min-height: 100vh !important;
    }

    .footer-container {
        height: 4em;
    }

    .footer {
        height: 4em;
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgb(119, 136, 153);
        text-align: center;
    }

    .footer-element {
        display: inline-block;
        overflow: hidden;
        height: 100%;
    }

    .icon {
        padding: 1em 1em 1em 1em;
        margin: 0;
        width: 2em;
        height: 2em;
        cursor: grab;
        overflow: hidden;
    }

    .vertical-line {
        padding: 0em 1em 0em 1em;
        display: inline-block;
        height: 100%
    }

    .inline-block {
        display: inline-block;
        height: 100%;
    }

    @media (max-width: 1100px) {}
</style>
