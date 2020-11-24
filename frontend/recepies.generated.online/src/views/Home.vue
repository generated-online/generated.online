<template>
    <div>
                <EmojieBackground :emojieSize='4' rowHeight="1.5em" emojiPadding="0.8em" :emojieAmount='8' />

        <div class="info-container">
            <h1 style="text-align:center; margin-bottom:2em; font-size: 5em"> <span class="text-span">
                KI generierte Rezepte!</span>
            </h1>
            <Search style="width: 77%; margin: auto" />
        </div>
    </div>
</template>

<script>
    import Search from "./Search";
    import EmojieBackground from "@/components/EmojieBackground"


    export default {
        name: "info",
        components: {
            Search,
            EmojieBackground
        },
        created() {
            this.$emit('shareText', "Schau dir diese coolen von einer KI generierten Rezepte an!");
            this.$emit('recipeId', null);
        }
    };
</script>

<style scoped>
    .info-container {
        text-align: left;
        height: 100% !important;
        padding: 2em 0em 2em 0em;
        max-width: 100vw !important;
        min-height: 100vh !important;
    }
</style>