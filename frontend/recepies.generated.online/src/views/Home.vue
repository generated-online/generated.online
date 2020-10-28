<template>
    <div>
        <div class="info-container">
            Hello our starting page here!
        </div>
    </div>
</template>

<script>
    export default {
        name: "info",
        created() {
            this.$emit('shareText', "Schau dir diese coolen von einer KI generierten Rezepte an!");
        }
    };
</script>

<style>
    body,
    #app {
        margin: 0;
        padding: 0;
        overflow-x: hidden;
        max-width: 100vw !important;
        min-height: 100vh !important;
    }

    .info-container {
        text-align: left;
        height: 100% !important;
        padding: 2em 2em 2em 2em;
        max-width: 100vw !important;
        min-height: 100vh !important;
    }

    @media (max-width: 1100px) {}
</style>