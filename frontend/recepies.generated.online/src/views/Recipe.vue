<template>
    <div>
        <v-card :class="['mb-16','info-container',{'mt-8':$vuetify.breakpoint.mdAndUp}]">
            <div v-if='recipe && loaded'>
                <!-- Title and Voting -->
                <div style="min-height: 100vh">
                    <v-container :class="['pb-6', 'pa-0']">
                        <v-row no-gutters>
                            <v-col>
                                <div :class="['text-sm-h3', 'text-md-h2', 'text-h4', {'text-center': $vuetify.breakpoint.xs}, 'boldy']"
                                     style="word-break: break-word">
                                    {{ recipe.title }}
                                </div>
                            </v-col>
                            <v-col align="center" cols="12" sm="auto">
                                <div :style="{'width': 'min-content', 'margin': 'auto', 'padding-top': $vuetify.breakpoint.xs? '1em':'0'}"
                                     class="ml-sm-4">
                                    <Voting :recipe='recipe'/>
                                </div>
                            </v-col>
                        </v-row>
                    </v-container>
                    <!-- Zutaten and Instructions -->
                    <v-container class="pa-0 pb-6">
                        <v-row no-gutters>
                            <!-- ZUTATEN -->
                            <v-col cols="12" lg="auto" md="auto">
                                <div :class="['text-sm-h6', 'text-md-h6', 'text-h6']"
                                     :style="{'margin':$vuetify.breakpoint.xs?'auto': '0'}">
                                    <v-container class="pa-0">
                                        <!-- starting from md the ingredients should only have the width of min content-->
                                        <v-row :justify="$vuetify.breakpoint.smAndDown?'center': 'start'"
                                               :style="{'width': ($vuetify.breakpoint.smAndDown)? 'auto':'min-content'}"
                                               no-gutters>
                                            <template v-for="(ingredient, n) in recipe.ingredients">
                                                <div :key="n" :class="['boldy','ma-1','py-1','px-4']"
                                                     :style="{'width': 'max-content'}">
                                                    {{ ingredient }}
                                                </div>
                                                <v-responsive v-if="!$vuetify.breakpoint.smAndDown" :key="`width-${n}`"
                                                              width="100%"></v-responsive>
                                            </template>
                                        </v-row>
                                    </v-container>
                                </div>
                            </v-col>
                            <!--  Instructions -->

                            <v-col class=" ml-md-6">
                                <span class="instruction text-span mt-3">
                                    {{ recipe.instructions }}
                                </span>
                            </v-col>
                        </v-row>
                    </v-container>
                </div>

                <!--  Postcard -->
                <PayPalPostcard :recipe='recipe'/>
            </div>
        </v-card>

        <div v-if="!loaded" class="loader">
            <img alt="loading animation" src="/robokoch.gif"
                 style="display:block; height: 100px; width: 100px; margin: auto; margin-top: 30vh">
        </div>
    </div>
</template>

<script>
import Voting from "@/components/Voting"
import EmojieBackground from "@/components/EmojieBackground"
import PayPalPostcard from "@/components/postcard-stuff/PayPalPostcard"
import {loadRecipe} from "@/functions/recipeUtils";

export default {
    name: "Recipe",
    components: {
        Voting,
        EmojieBackground,
        PayPalPostcard
    },
    data() {
        return {
            recipe: undefined,
            loaded: false,
        };
    },
    created() {
        loadRecipe(this.$route.params.id).then((recipe) => {
            this.recipe = recipe;
            this.loaded = true;
            this.$emit('shareText', 'Schau dir dieses coole KI generierte Rezept an: ' + this.recipe['title']);
            this.$emit('recipe', this.recipe);
        });

    }
};
</script>

<style lang="scss" scoped>
.loader {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--bg-color);
}

.instruction {
  animation: fade-in 1s forwards;
  -webkit-animation: fade-in 1s forwards;
  opacity: 0;
  background: rgba(0, 0, 0, 1);
  color: var(--bg-color);
  border-radius: 15px;
  padding: 15px;
  font-size: 1.5em;
  text-align: justify;
  display: block;
}
</style>