<template>
    <span>
        <!-- if there is text we want to have a real button -->
        <v-btn v-if="buttonText !== ''" to="/recipe" large color="lime accent-4 black--text" class="boldyAppearing my-6 bg-green" >
            <h2 style="text-transform: capitalize !important"> {{ buttonText }}</h2>
            <v-icon style="padding-left:0.5em">shuffle</v-icon>
        </v-btn>
        <!-- without text no button -->
        <v-btn v-if="buttonText === ''" to="/recipe" icon class="mx-3 my-0">
            <v-icon class="vue-icon">shuffle</v-icon>
        </v-btn>
    </span>

</template>


<script>
export default {
    name: "big-footer",
    props: {
        "buttonText": {
            type: String,
            default: "Zufälliges Rezept"
        },
    },
}
</script>