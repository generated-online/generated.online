<template>
    <v-footer fixed padless style="background: transparent; pointer-events: none;">
        <v-card class="footer-container text-center" flat style="background: transparent" tile width="100%">
            <v-card-text :style="{'margin-right': $vuetify.breakpoint.smAndDown? '0.3em':'auto',
            'width': $vuetify.breakpoint.smAndDown? 'min-content':'max-content'}"
                         class="py-1 px-0 text center allIcons">
                <v-btn class="mx-2 my-1 boldy remove-acive" icon to="/">
                    <v-icon class="vue-icon" size="30">search</v-icon>
                </v-btn>

                <v-btn class="mx-1 my-1 boldy" icon to="/recipe">
                    <v-icon class="vue-icon">shuffle</v-icon>
                </v-btn>

                <v-btn class="mx-1 my-1 boldy" icon to="/highscore">
                    <img :src="getImgUrl('womanCook')" :style="{'filter': 'hue-rotate('+(nameToHSL(color)-43)+'deg)'}" class="vue-icon">
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
    },
    methods: {
        getImgUrl,
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

            return  h
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
  //color: transparent;
  //text-shadow: 0 0 0 var(--bg-color);
  height: 1.5em;
}

.allIcons {
  margin-left: auto;
  background: var(--bg-color);
  border-radius: 35px !important;
  pointer-events: all;
  margin-bottom: 0.3em;
  height: max-content;
}
</style>