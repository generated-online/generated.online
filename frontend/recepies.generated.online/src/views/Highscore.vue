<template>
    <v-container>
        <v-row align="center" justify="center" class="text-h2 boldy mb-8 text-center" style="font-weight:bold;">
            <img src="../assets/robokoch.png" class="emoji">
            Beschde Rezepte
        </v-row>
        <v-row v-for="recipe in recipes" :style="{'color':(recipeToColor(recipe.id) +' !important')}" class="row"
            no-gutters :key="recipe.id">
            <router-link :to="'/recipe/' + recipe.id" class="boldyNoColor px-4 py-1 mb-4" style="width:100%">
                <v-row cols="12" no-gutters align="center">
                    <v-col align="center" class="text-h3" cols="auto" style="min-width: 1.75em">
                        {{ recipe.votes }}
                    </v-col>
                    <v-col class="ml-2">
                        <v-row class="text-h6">
                            {{ recipe.title }}
                        </v-row>
                        <v-row class="mb-1 text-h6">
                            <img v-for="emoji in recipeToEmojis(recipe).map(getImgUrl)" :src="emoji" class="emoji pr-2" :key="emoji">
                        </v-row>
                    </v-col>

                </v-row>
            </router-link>
        </v-row>
    </v-container>
</template>

<script>
    import firebase from "firebase";
    import recipeToColor from "@/functions/recipe_to_color";
    import {
        recipeToEmojis,
        getImgUrl
    } from "@/functions/emojiUtils"

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
            getImgUrl
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