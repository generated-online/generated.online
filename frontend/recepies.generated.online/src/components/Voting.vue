<template>
    <v-container class="boldyAppearing text-sm-subtitle-1 text-md-h5 text-subtitle-2 text-center">
        <b>Bewertungen</b>
        <div style="width:max-content; display:flex; margin: auto">
            <h1 class="verticalCenter"> {{ recipe.votes }}
            </h1>
            <v-btn class="transparentButton verticalCenter" :disabled="!possibleToVote" :loading="buttonLoading" fab
                dark small color="transparent" @click="upvote">
                <img src="../assets/robokoch.png" alt="cooking robot" class="color-adapt" style="vertical-align:middle; height: 1em">
            </v-btn>
        </div>
    </v-container>
</template>

<script>
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
                            this.$analytics.logEvent('voted')
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
        width: 1.5em;
        height: 1.5em;
        font-size: 2em;
    }

    .horizontalLine {
        width: 100%;
        background-color: black;
        opacity: 0.6;
        height: 1px;
        font-size: 1px;
    }

    .verticalCenter {
        display: flex;
        align-items: center;
    }
</style>