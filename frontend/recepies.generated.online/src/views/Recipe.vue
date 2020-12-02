<template>
    <v-card class="info-container recipe-container">
        <div v-if='recipe'>
            <v-container class="pb-6">
                <v-row
                        no-gutters
                >
                    <v-col>
                        <div :class="['text-sm-h3', 'text-md-h2', 'text-h4', {'text-center': $vuetify.breakpoint.xs}]"
                             style="word-break: break-word">
                            {{ recipe.title }}
                        </div>
                    </v-col>
                    <v-col cols="12" sm="auto">
                        <div :style="{'width': 'fit-content', 'margin': 'auto', 'padding-top': $vuetify.breakpoint.xs? '1em':'0'}">
                            <Voting :recipe='recipe'/>
                        </div>
                    </v-col>
                </v-row>
            </v-container>
            <v-container class="pb-6">
                <v-row
                        no-gutters
                >
                    <v-col cols="12" md="auto" lg="auto">
                        <!-- ZUTATEN -->
                        <div :class="['text-sm-h6', 'text-md-h6', 'text-h6']"
                             :style="{'margin':$vuetify.breakpoint.xs?'auto': '0'}">
                            <v-container>
                                <!--                                starting from md the ingredients should only have the width of min content-->
                                <v-row no-gutters
                                       :style="{'width': ($vuetify.breakpoint.sm)? 'auto':'min-content'}">
                                    <template v-for="(ingredient, n) in recipe.ingredients">
                                        <v-col :key="n"
                                               :style="{
                                            'width': 'max-content',
                                            'border-left': (n%2 === 1 && $vuetify.breakpoint.smOnly)?'1px solid rgba(0,0,0, 0.3)':'',
                                            'padding-left': (n%2 === 1 && $vuetify.breakpoint.smOnly) ?'1em':'0'
                                        }">
                                            {{ ingredient }}
                                        </v-col>
                                        <v-responsive
                                                v-if="n%2 === 1 || !$vuetify.breakpoint.smOnly"
                                                :key="`width-${n}`"
                                                width="100%"
                                        ></v-responsive>
                                    </template>
                                </v-row>
                            </v-container>
                        </div>
                    </v-col>
                    <v-divider vertical inset v-if="!$vuetify.breakpoint.smAndDown"
                               style="margin-right: 1em"></v-divider>
                    <v-col>
                        <!--  Instructions -->
                        <span class="instruction text-span">
            {{ recipe.instructions }}
          </span>
                    </v-col>
                </v-row>
            </v-container>
            <v-divider></v-divider>

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


.instruction {
    font-size: 1.5em;
    /*flex-grow: 1;*/
    text-align: justify;
    display: block;
    /*padding: 2%;*/
    /*margin-left: 2%;*/
}

</style>