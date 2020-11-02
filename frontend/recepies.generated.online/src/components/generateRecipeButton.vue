<template>
    <span>
        <!-- if there is text we want to have a real button -->
        <v-btn v-if="buttonText !== ''" to="/recipe" depressed outlined style="background: white; opacity: 0.8"
            class="mx-3 my-0">
            {{buttonText}}
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