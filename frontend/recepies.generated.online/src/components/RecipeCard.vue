<template>
    <v-hover v-slot="{ hover }">
        <router-link :to="'/recipe/' + internalRecipe.id"
                     class="boldyNoColor px-4 py-1 mb-4"
                     style="width:100%">
            <v-row :style="'color: '+ recipeColor"
                   align="center"
                   cols="12" no-gutters>
                <v-col align="center" class="text-h3" cols="auto" style="min-width: 1.75em">
                    <img v-if="!internalRecipe.votes" class="small-emoji" src="/robokoch.gif">
                    <span v-else> {{ internalRecipe.votes }}</span>
                </v-col>
                <v-col class="ml-2">
                    <v-row class="text-h6 font-weight-bold">
                        {{ internalRecipe.title }}
                    </v-row>

                    <v-expand-transition appear>
                        <v-row v-if="!hover" key="emojis" class="mb-1 text-h6">
                            <img v-for="emoji in recipeToEmojis(internalRecipe).map(getImgUrl)" :key="emoji"
                                 :src="emoji"
                                 class="small-emoji pr-2">
                        </v-row>
                        <v-row v-else key="ingredients" class="mb-1 ">
                            <v-col v-for="ingredient in internalRecipe.ingredients"
                                   align="center"
                                   class="pa-0 ma-0 ingredient--hovered"
                                   cols="auto"
                                   justify="center"
                            >
                                <Ingredient :class="['boldy','ma-1','py-0','px-2']"
                                            :ingredient="ingredient"
                                            :style="'background-color:'+recipeColor"
                                            style="color:black !important; height:fit-content"/>
                            </v-col>
                        </v-row>
                    </v-expand-transition>
                </v-col>
            </v-row>
        </router-link>
    </v-hover>
</template>
<script>
import {getImgUrl, recipeToEmojis, wordToEmoji} from "@/functions/emojiUtils"
import {loadRecipe} from "@/functions/recipeUtils";
import recipe_to_color from "@/functions/recipe_to_color";
import Ingredient from "@/components/Ingredient";


export default {
    name: 'RecipeCard',
    components: {Ingredient},
    props: {
        recipe: {},
    },
    data() {
        return {
            internalRecipe: this.recipe,
            recipeColor: recipe_to_color(this.recipe.id)
        }
    },
    methods: {
        getImgUrl,
        recipeToEmojis,
        wordToEmoji
    },
    mounted() {
        if (this.recipe.votes === "") {
            loadRecipe(this.recipe.id).then((recipe) => {
                this.internalRecipe.votes = recipe.votes
            })
        }
    }
}
</script>
<style scoped>
a {
    text-decoration: none;
    color: inherit !important;
}

/*add opacity to animation*/
/*enter and leave are start points of transition; both *-to are endpoint of transition*/
.expand-transition-enter,  .expand-transition-leave-to{
    opacity: 0;
}

.expand-transition-enter-to, .expand-transition-leave {
    opacity: 1;
}

/* control animation duration with this: */
/*.expand-transition-enter-active,*/
/*.expand-transition-leave-active{*/
/*    transition-duration: 2s !important;*/
/*}*/

</style>