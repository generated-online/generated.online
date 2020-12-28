<template>
    <div :style="{'width': 'max-content'}">
        <span v-if="placeEmojiLeft" v-for="emoji in emojis">
            <img class="small-emoji mr-1" :src="emoji" >
        </span>
        <span >
            {{ingredient}}
        </span>
        <span  v-if="!placeEmojiLeft" v-for="emoji in emojis">
            <img class="small-emoji ml-1" :src="emoji" >
        </span>
    </div>
</template>

<script>
import {sentenceToEmoji} from "@/functions/emojiUtils";

export default {
    name: "Ingredient",
    props: {"ingredient": String, "placeEmojiLeft": {type: Boolean, default: true}},
    data() {
        return {
            emojis: []
        }
    },
    created() {
        this.emojis = sentenceToEmoji(this.ingredient)
    }
}
</script>

<style scoped>
</style>