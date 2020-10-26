<template>
    <div>
        <div class="info-container">
            Hier wird demnächst super info stehen!
        </div>
        <Footer />
    </div>

</template>

<script>
    import Footer from "./Footer";
    export default {
        name: "info",
        components: {
            Footer
        },
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