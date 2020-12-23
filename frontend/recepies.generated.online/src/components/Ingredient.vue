<template>
    <div
         :style="{'width': 'max-content'}">
        <div v-if="ingredientSplit">
            <span>{{ ingredientSplit[0] }}</span>
            <img class="small-emoji" :src="ingredientSplit[1]" >
            <span>{{ ingredientSplit[2] }}</span>
        </div>
        <span v-else>
            {{ingredient}}
        </span>
    </div>
</template>

<script>
import {wordToEmoji} from "@/functions/emojiUtils";

export default {
    name: "Ingredient",
    props: ["ingredient"],
    data() {
        return {
            ingredientSplit: false
        }
    },
    created() {
        this.ingredientSplit = wordToEmoji(this.ingredient)
    }
}
</script>

<style scoped>
</style>