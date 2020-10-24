<template>
    <div class="container">
        Hello, hier is some awsome information!
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

    @media (max-width: 1100px) {}
</style>
