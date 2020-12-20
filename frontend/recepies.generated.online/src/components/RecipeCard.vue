<template>
    <router-link :to="'/recipe/' + recipe.id" class="boldyNoColor px-4 py-1 mb-4" style="width:100%">
        <v-row align="center" cols="12" no-gutters>
            <v-col align="center" class="text-h3" cols="auto" style="min-width: 1.75em">
                {{ recipe.votes }}
            </v-col>
            <v-col class="ml-2">
                <v-row class="text-h6">
                    {{ recipe.title }}
                </v-row>
                <v-row class="mb-1 text-h6">
                    <img v-for="emoji in recipeToEmojis(recipe).map(getImgUrl)" :key="emoji" :src="emoji" class="emoji pr-2">
                </v-row>
<!--                todo: hover show ingredients-->
            </v-col>
        </v-row>
    </router-link>
</template>
<script>
import {getImgUrl,recipeToEmojis} from "@/functions/emojiUtils"

export default {
    name: 'RecipeCard',
    props: {
        recipe: {},
    },
    methods: {
        getImgUrl,
        recipeToEmojis
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