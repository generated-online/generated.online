<template>
    <div class="postcard-container">
        <div class="postcard-body" :style="'background:'+ color ">
            <EmojieBackground :recipe="recipe" />
            <p class="ad text-span">gesendet von recipes.generated.online</p>
            <div class="postcard-inner">
                <span>
                    <h1 class="text-span">{{recipe.title}}</h1>
                </span>
            </div>
        </div>

        <div class="postcard-body" style="background:white ">
            <div class="postcard-inner-back">
                <div class="half-postcard instructions">
                    <h2>{{recipe.title}}</h2>
                    <p v-for="ingredient in recipe.ingredients" v-bind:key="ingredient">{{ingredient}}</p>
                    <p>{{recipe.instructions}}</p>
                    <p>Gesendet von recipes.generated.online</p>
                </div>
                <div class="half-postcard">
                    <div class="stamp"></div>
                    <div class="address">
                        <input type="text" placeholder="Name" v-model="name" disabled>
                        <input type="text" placeholder="Straße" v-model="street" disabled>
                        <input type="text" placeholder="Postleitzahl und Ort" v-model="zip" disabled>
                        <input type="text" placeholder="Land" v-model="country" disabled>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    import EmojieBackground from "@/components/EmojieBackground"

    export default {
        props: ['recipe', 'color', 'name', 'street', 'zip', 'country'],
        components: {
            EmojieBackground,
        }
    }
</script>

<style scoped>
    @media (max-width: 1100px) {
        .postcard-body {
            float: left !important;
        }

        .postcard-container {
            height: 200% !important;
            width: 600vw !important;
        }

    }

    .postcard-container {
        width: 100vw;
        height: 400%;
    }

    .instructions {
        padding-top: 70px;
        padding-right: 10px;
    }

    .stamp {
        position: absolute;
        width: 145px;
        height: 190px;
        border: dashed black 2px;
        background: whitesmoke;
        right: 0;
    }

    input,
    .input {
        padding-top: 10px;
        margin-top: 10px;
        width: 50%;
        margin-right: 40%;
        margin-left: 10%;
        background: whitesmoke;
        border: dashed black 2px;
        float: right;
        display: block;
    }

    .address {
        border-left: solid black 4px;
        position: absolute;
        top: 300px;
        padding-top: 150px;
        left: 0;
    }

    .address input {
        padding-left: 1em
    }

    .half-postcard {
        position: relative;
        width: 50%;
        float: left;
    }

    .postcard-body {
        margin-right: 80px !important;
        float: left;
        position: relative;
        margin-top: 50px !important;
        margin: auto;
        border: solid black 40px;
        width: 1440px;
        height: 1040px;
    }

    .postcard-inner {
        position: relative;
        padding: 140px;
    }

    .postcard-inner-back {
        padding: 30px;
    }

    .ad {
        position: absolute;
        left: 140px;
        bottom: 0;
    }

    h1 {
        font-size: 120px;
        position: absolute;
    }

    p {
        font-size: 18px;
    }

    h2 {
        padding-bottom: 10px;
    }
</style>