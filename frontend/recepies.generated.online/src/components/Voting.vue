<template>
    <span class="vote-container">
        <v-card class="pb-1 vcard" elevation="0" :style='"background: "+ color + ";"'>
            <span class="mx-4"> {{recipe.votes}} </span>
            <v-btn class="transparentButton mx-4" :disabled="!possibleToVote" :loading="buttonLoading" fab dark small
                color="transparent" @click="upvote">
                <span class="womanCook">👩‍🍳</span>
            </v-btn>
        </v-card>
    </span>

</template>

<script>
    import firebase from "firebase";
    import recipeToColor from "@/functions/recipe_to_color";

    export default {
        props: {
            "recipe": {
                type: Object,
                default: null
            }
        },
        data() {
            return {
                possibleToVote: !this.$cookies.isKey(this.recipe.id),
                buttonLoading: false,
                color: recipeToColor(this.recipe.id),
            };

        },
        methods: {
            upvote() {
                if (!this.$cookies.isKey(this.recipe.id)) {

                    // this makes sure the button is not pressed multiple times
                    this.buttonLoading = true

                    var xhr = new XMLHttpRequest()
                    xhr.open('POST', 'https://x8fzkq5471.execute-api.us-east-2.amazonaws.com/default/upvote')
                    xhr.onerror = () => {
                        console.log('Error calling api', xhr.response)
                    }
                    xhr.onreadystatechange = () => {
                        // we get an response and teh request was sucessfull
                        if (xhr.readyState === 4 && xhr.status === 200) {
                            this.$cookies.set(this.recipe.id)
                            this.recipe.votes += 1
                            this.possibleToVote = false
                        }

                        // and enable the button again
                        this.buttonLoading = false
                    }
                    xhr.send(JSON.stringify({
                        "id": this.recipe.id
                    }))


                }
            }
        },
        computed: {
            iconStyle() {
                if (this.possibleToVote) {
                    return {
                        "cursor": "grab",
                        "color": "rgb(255, 0,0) !important"
                    }
                } else {
                    return {
                        "cursor": "not-allowed",
                        "color": "rgba(0.82745098039, 0.82745098039, 0.82745098039, 0.6) !important"
                    }
                }
            }
        }
    }
</script>

<style scoped>
    .transparentButton {
        margin-left: 20px;
        width: calc(70vw / 15*1.3);
        height: calc(70vw / 15*1.3);
        vertical-align: baseline;
        font-size: inherit;
    }

    .vote-container {
        text-align: center;
        width: fit-content;
        font-family: "Commissioner";
    }

    .vcard {
        border: thin solid black;
        margin: auto;
    }

    @media (max-width: 800px) {
        .transparentButton {
            width: calc(70vw / 8*1.3);
            height: calc(70vw / 8*1.3);
        }

        .vcard {
            width: fit-content;
        }
    }
</style>