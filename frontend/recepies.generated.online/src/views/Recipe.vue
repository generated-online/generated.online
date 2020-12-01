<template>
    <v-card class="info-container recipe-container">
        <div v-if='recipe'>
            <v-container>
                <v-row
                        no-gutters
                >
                    <v-col>
                        <div :class="['text-sm-h3', 'text-md-h2', 'text-h4', 'pb-12', {'text-center': $vuetify.breakpoint.xs}]"
                             style="word-break: break-word">
                            {{ recipe.title }}
                        </div>
                    </v-col>
                    <v-col cols="12" sm="auto">
                        <div :style="{'width': $vuetify.breakpoint.xs? '30%':'100%', 'margin': 'auto'}">
                            <Voting style="border: 1px solid black" :recipe='recipe'/>
                        </div>
                    </v-col>
                </v-row>
            </v-container>
            <!--            <div class="title-container">-->
            <!--                <h1 class="recipe-title text-span dynamic-font-size">-->
            <!--                    {{ recipe.title }}-->
            <!--                </h1>-->
            <!--                <Voting class="recipe-vote dynamic-font-size text-span" :recipe='recipe'/>-->
            <!--            </div>-->

            <div class="recipe-body">
                <!-- ZUTATEN -->
                <div class="ingredients text-span">
                    <div class="ingredient" :key="ingredient+String(Math.floor(Math.random() * 100))"
                         v-for="ingredient in recipe.ingredients">
                        <span>{{ ingredient }}</span>
                    </div>
                    <div class="divider"></div>
                </div>
                <!--  Instructions -->
                <span class="instruction text-span">
            {{ recipe.instructions }}
          </span>
            </div>
            <!--  Postcard -->
            <PayPalPostcard :recipe='recipe'/>
        </div>
    </v-card>
</template>

<script>
import firebase from "firebase";
import Voting from "@/components/Voting"
import EmojieBackground from "@/components/EmojieBackground"
import PayPalPostcard from "@/components/PayPalPostcard"

export default {
    name: "recipe",
    components: {
        Voting,
        EmojieBackground,
        PayPalPostcard
    },
    data() {
        return {
            id: "",
            recipe: undefined,
            error: "",
        };
    },
    created() {
        let db = firebase.firestore();
        const ref = db.collection("recipes")

        this.id = this.$route.params.id;
        let key = "";
        if (typeof this.id !== "undefined") {
            ref
                .doc(this.id)
                .get()
                .then((doc) => {
                    this.loadData(doc);
                });
        } else {
            key = ref.doc().id;
            ref
                .where(firebase.firestore.FieldPath.documentId(), ">=", key)
                .limit(1)
                .get()
                .then((snap) => {
                    if (snap.size === 0) {
                        ref
                            .where(firebase.firestore.FieldPath.documentId(), "<", key)
                            .limit(1)
                            .get()
                            .then((snap) => {
                                snap.docs.map(this.loadData);
                            });
                    } else {
                        snap.docs.map(this.loadData);
                    }
                })
                .catch((err) => {
                    this.error = err;
                });
        }
    },
    methods: {
        loadData(doc) {
            this.recipe = {
                id: doc.id,
                ingredients: doc.data().ingredients,
                title: doc.data().title,
                instructions: doc.data().instructions,
                votes: doc.data().votes || 0,
            };

            this.$emit('shareText', 'Schau dir dieses coole KI generierte Rezept an: ' + this.recipe['title']);
            // this.$emit('recipeId', this.recipe.id);
            this.$emit('recipe', this.recipe);
            if (this.id === undefined) {
                this.$router.replace("/recipe/" + doc.id);
            }
        },
    }
};
</script>

<style scoped>
.recipe-container {
    padding: 2em
}

.dynamic-font-size {
    font-size: calc(70vw / 15);
    font-family: "Commissioner", serif;
    padding: 0.2em 0.2em 0.2em 0.2em;
}

.recipe-title {
    word-wrap: break-word;
    /*flex-grow: 1;*/
    /*margin-right: 0.5em*/
}

.recipe-vote {
    float: right;
    height: fit-content;
}

.recipe-body {
    padding-bottom: 1.5em;
    display: flex;
}

.ingredient {
    padding-bottom: 0.5em;
    font-size: 1.2em;
    white-space: nowrap
}

.ingredients {
    width: fit-content;
    padding: 2%
}

.instruction {
    font-size: 1.5em;
    flex-grow: 1;
    text-align: justify;
    display: block;
    padding: 2%;
    margin-left: 2%;
}

@media (max-width: 800px) {
    .dynamic-font-size {
        font-size: calc(70vw / 8);
    }

    .title-container {
        text-align: center;
        display: block;
        align-items: center;
    }

    .recipe-title {
        /*word-wrap: break-word;*/
        /*text-align: center;*/
        /*flex-grow: 0;*/
        /*width: 80%;*/
        /*margin: auto;*/
        /*margin-bottom: 0.5em;*/
    }

    .recipe-vote {
        float: unset;
        width: fit-content;
        height: fit-content;
        margin: auto;
    }

    .recipe-body {
        position: relative;
        overflow: hidden;
        display: block;
    }

    .ingredient {
        padding-bottom: 0.5em;
        width: 50%;
        float: left;
    }

    .ingredients {
        width: 100%;
        margin-bottom: 2em;
        float: left;
        position: relative;
    }

    .instruction {
        float: left;
        margin-left: 0;
    }

    .divider {
        position: absolute;
        left: 48%;
        top: 5%;
        bottom: 5%;
        border-left: 3px solid black;
    }
}

@media (min-width: 500px) and (max-width: 600px) {
    .ingredient {
        font-size: 1em;
        padding-bottom: 0.5em;
        width: 50%;
        float: left;
    }

    .divider {
        border-left: 1.5px solid black
    }
}

@media (max-width: 500px) {
    .ingredient {
        font-size: 1.4em;
        padding-bottom: 0.5em;

        width: 100%;
        float: none;

    }

    .divider {
        border-left: none;
    }
}
</style>