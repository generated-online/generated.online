<template>

</template>

<script>
import {getRandomRecipeID} from "@/functions/getRandomRecipe";

export default {
    name: "GetRandomRecipe",
    async beforeRouteEnter(to, from, next) {
        let recipeID = await getRandomRecipeID();
        next({"name": "specific-recipe", "params":{"id":recipeID}})
    }
};
</script>