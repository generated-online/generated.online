<template>
    <router-link :to="'/recipe/' + internalRecipe.id" class="boldyNoColor px-4 py-1 mb-4" style="width:100%">
        <v-row align="center" cols="12" no-gutters>
            <v-col align="center" class="text-h3" cols="auto" style="min-width: 1.75em">
                <img v-if="!internalRecipe.votes" class="emoji" src="/robokoch.gif">
                <span v-else> {{ internalRecipe.votes }}</span>
            </v-col>
            <v-col class="ml-2">
                <v-row class="text-h6">
                    {{ internalRecipe.title }}
                </v-row>
                <v-row class="mb-1 text-h6">
                    <img v-for="emoji in recipeToEmojis(internalRecipe).map(getImgUrl)" :key="emoji" :src="emoji"
                         class="emoji pr-2">
                </v-row>
            </v-col>
        </v-row>
    </router-link>
</template>
<script>
import {getImgUrl, recipeToEmojis} from "@/functions/emojiUtils"
import {loadRecipe} from "@/functions/recipeUtils";


export default {
    name: 'RecipeCard',
    props: {
        recipe: {},
    },
    data() {
        return {
            internalRecipe: this.recipe
        }
    },
    methods: {
        getImgUrl,
        recipeToEmojis
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

.emoji {
    vertical-align: middle;
    height: 1em;
}
</style>