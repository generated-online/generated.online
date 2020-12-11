<template>
    <v-card :class="['mb-16','info-container',{'mt-8':$vuetify.breakpoint.mdAndUp}]">
        <div v-if='recipe'>
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
                        <v-col cols="12" sm="auto">
                            <div
                                :style="{'width': 'fit-content', 'margin': 'autp', 'padding-top': $vuetify.breakpoint.xs? '1em':'0'}" class="ml-4">
                                <Voting :recipe='recipe' />
                            </div>
                        </v-col>
                    </v-row>
                </v-container>
                <!-- Zutaten and Instructions -->
                <v-container class="pa-0 pb-6" >
                    <v-row no-gutters>
                        <!-- ZUTATEN -->
                        <v-col cols="12" md="auto" lg="auto">
                            <div :class="['text-sm-h6', 'text-md-h6', 'text-h6']"
                                :style="{'margin':$vuetify.breakpoint.xs?'auto': '0'}">
                                <v-container>
                                    <!-- starting from md the ingredients should only have the width of min content-->
                                    <v-row no-gutters
                                        :style="{'width': ($vuetify.breakpoint.sm)? 'auto':'min-content'}">
                                        <template v-for="(ingredient, n) in recipe.ingredients">
                                            <div :key="n" :style="{'width': 'max-content'}" :class="['boldy','ma-1','py-1','px-4']">
                                                {{ ingredient }}
                                            </div>
                                             <v-responsive v-if="!$vuetify.breakpoint.smAndDown" :key="`width-${n}`" width="100%"></v-responsive>
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
            <PayPalPostcard :recipe='recipe' />
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

<style scoped lang="scss">
    .instruction {
        background: rgba(0, 0, 0, 1);
        color: var(--bg-color);
        border-radius: 15px;
        padding: 15px;
        font-size: 1.5em;
        text-align: justify;
        display: block;
    }
</style>