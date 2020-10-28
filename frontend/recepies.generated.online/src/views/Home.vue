<template>
    <div>
        <div class="info-container">
            <h1 style="text-align:center; margin-bottom:1em"> KI generierte Rezepte! </h1>
            <Search />
        </div>
    </div>
</template>

<script>
    import Search from "./Search";

    export default {
        name: "info",
        components: {
            Search
        },
        created() {
            this.$emit('shareText', "Schau dir diese coolen von einer KI generierten Rezepte an!");
        }
    };
</script>

<style scoped>
    .info-container {
        text-align: left;
        height: 100% !important;
        padding: 2em 2em 2em 2em;
        max-width: 100vw !important;
        min-height: 100vh !important;
    }
</style>