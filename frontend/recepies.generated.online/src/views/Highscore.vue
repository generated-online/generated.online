<template>
    <v-container>
        <div class="text-h2 boldy mb-8 text-center" style="font-weight:bold">👩‍🍳 Beschde Rezepte</div>
        <v-row v-for="recipe in recipes" :style="{'color':(recipeToColor(recipe.id) +' !important')}" class="row"
               no-gutters>
            <router-link :to="'/recipe/' + recipe.id" class="boldyNoColor px-4 py-1 mb-4" style="width:100%">
                <v-row cols="12" no-gutters>
                    <v-col align="center" class="text-h3" cols="auto" style="min-width: 1.75em">
                        {{ recipe.votes }}
                    </v-col>
                    <v-col class="text-h6">
                        {{ recipe.title }}
                    </v-col>
                </v-row>
            </router-link>
        </v-row>
    </v-container>
</template>

<script>
import firebase from "firebase";
import recipeToColor from "@/functions/recipe_to_color";

export default {
    name: "MostViewedRecipes",
    components: {},
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
        console.log(this.num_recipes)
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
        recipeToColor
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

</style>