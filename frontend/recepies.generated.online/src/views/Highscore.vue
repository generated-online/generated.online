<template>
    <v-container>
        <v-row align="center" class="text-h2 boldy mb-8 text-center" justify="center" style="font-weight:bold;">
            <img class="emoji" src="/robokoch.gif">
            Beschde Rezepte
        </v-row>
        <v-row v-for="recipe in recipes" :key="recipe.id" :style="{'color':(recipeToColor(recipe.id) +' !important')}"
               class="row"
               no-gutters>
            <RecipeCard :recipe="recipe" :recipe-to-emojis="recipeToEmojis(recipe)"/>
        </v-row>
    </v-container>
</template>

<script>
import firebase from "firebase";
import recipeToColor from "@/functions/recipe_to_color";
import {recipeToEmojis} from "@/functions/emojiUtils"
import RecipeCard from "@/components/RecipeCard";

export default {
    name: "MostViewedRecipes",
    components: {RecipeCard},
    props: {
        "num_recipes": {
            type: Number,
            default: 10
        }
    },
    data() {
        return {
            recipes: [],
        };
    },
    created() {
        let db = firebase.firestore();
        const ref = db.collection("recipes")
        ref.orderBy("votes", "desc").limit(this.num_recipes)
            .get()
            .then((snap) => {
                if (snap.size === 0) {
                    console.log("No highscores found")
                } else {
                    snap.docs.map(this.loadData);
                }
            }).catch((err) => {
            console.error(err)
        });
        this.$emit('shareText', "Schau dir diese bestbewerteten von einer KI generierten Rezepte an!");
        this.$emit('recipe', null);
    },
    methods: {
        loadData(doc) {
            this.recipes.push({
                id: doc.id,
                ingredients: doc.data().ingredients,
                title: doc.data().title,
                instructions: doc.data().instructions,
                votes: doc.data().votes || 0,
            });
        },
        recipeToColor,
        recipeToEmojis,
    }
}
</script>

<style scoped>
a {
    text-decoration: none;
    color: inherit !important;
}

.row {
    font-weight: bold;

}

.emoji {
    vertical-align: middle;
    height: 1em;
}
</style>