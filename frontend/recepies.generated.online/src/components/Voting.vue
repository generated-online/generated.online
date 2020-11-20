<template>
    <span class="vote-container">
        <v-btn class="mx-3 my-3 pa-8 transparentButton" :disabled="!possibleToVote" fab dark small color="transparent"
            @click="upvote">
            <span class="nbVotes" style="color: darkred !important; font-size: 22px">{{recipe.votes}}</span>
            <v-icon size="70" :style="cssVars">favorite_border</v-icon>
        </v-btn>
    </span>

</template>

<script>
    import firebase from "firebase";
    export default {
        props: {
            "recipe": {
                type: Object,
                default: null
            }
        },
        data() {
            return {
                possibleToVote: !this.$cookies.isKey(this.recipe.id)
            };

        },
        methods: {
            upvote() {
                if (!this.$cookies.isKey(this.recipe.id)) {

                    var xhr = new XMLHttpRequest()
                    xhr.open('POST', 'https://x8fzkq5471.execute-api.us-east-2.amazonaws.com/default/upvote')
                    xhr.onerror = () => {
                        console.log('Error calling api', xhr.response)
                    }
                    xhr.onreadystatechange = () => {
                        if (xhr.readyState === 4 && xhr.status === 200) {
                            this.$cookies.set(this.recipe.id)
                            this.recipe.votes += 1
                            this.possibleToVote = false
                        }
                    }
                    xhr.send(JSON.stringify({
                        "id": this.recipe.id
                    }))
                }
            }
        },
        computed: {
            cssVars() {

                if (this.possibleToVote) {
                    return {
                        "cursor": "grab",
                        "color": "rgb(255, 0, 0) !important"
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
        box-shadow: none;
    }

    .nbVotes {
        position: absolute;
        z-index: 99;
    }

    .vote-container {
        text-align: center;
        width: 100%;
    }
</style>