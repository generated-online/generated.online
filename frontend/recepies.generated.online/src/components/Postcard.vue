<template>
    <div class="postcard-container" :style="'transform: scale(' + scaling()+'); transform-origin: top left'">
        <div class="postcard-body postcard-cover">
            <EmojieBackground :recipe="recipe" :opacity="1"/>
            <div class="postcard-inner">
                <span>
                    <h1>{{ recipe.title }}</h1>
                </span>
                <span class="ad adPositionFront">gesendet mit recipes.generated.online</span>
            </div>
        </div>

        <div class="postcard-body" style="background:white ">
            <div class="postcard-inner-back">
                <div class="half-postcard">
                    <h2>{{ recipe.title }}</h2>
                    <p v-for="ingredient in recipe.ingredients" v-bind:key="ingredient">{{ ingredient }}</p>
                    <br>
                    <p style="text-align: justify">{{ recipe.instructions }}</p>
                    <br>
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
                <p class="ad adPositionBack">gesendet mit recipes.generated.online</p>
            </div>
        </div>
    </div>

</template>

<script>
import EmojieBackground from "@/components/EmojieBackground"

export default {
    props: {
        "recipe": {
            type: Object,
            default: {}
        },
        "name": {
            type: String,
            default: ""
        },
        "street": {
            type: String,
            default: ""
        },
        "zip": {
            type: String,
            default: ""
        },
        "country": {
            type: String,
            default: "DE"
        },
        "horizontal": {
            type: Boolean,
            default: true
        },
        "parentWidth": {
            type: Number,
            default: 100.
        }

    },
    data() {
        return {
            scalingFactor: 0.1
        }
    },
    components: {
        EmojieBackground,
    },
    methods: {
        scaling() {
            let scaleFactor
            if (!this.horizontal) {
                scaleFactor = this.parentWidth / 1440
                this.$emit("height", scaleFactor*(1040*2))
            } else {
                scaleFactor = this.parentWidth / (1440 * 2)
                this.$emit("height", scaleFactor*(1040))

            }
            return scaleFactor
        }
    },
    mounted() {
        this.scalingFactor = this.scaling()
    }
}
</script>

<style scoped>

.postcard-container {
    height: 100%;
    width: min-content;
}

p {
    margin: 0 !important;
    padding: 0 !important
}

.stamp {
    position: absolute;
    width: 145px;
    height: 190px;
    border: dashed black 2px;
    background: whitesmoke;
    right: 4%;
}

input,
.input {
    padding-top: 10px;
    margin-top: 10px;
    width: 70%;
    margin-right: 20%;
    margin-left: 10%;
    background: whitesmoke;
    border: dashed black 2px;
    float: right;
    display: block;
    font-size: 2em;
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
    height: 100%;
    padding: 2%;
}

.postcard-cover {
    margin-bottom: 50px;
}

.postcard-body {
    float: left;
    position: relative;
    border: solid black 40px;
    width: 1440px;
    height: 1040px;
}

.postcard-inner {
    padding: 140px;
    height: 100%;
}

.postcard-inner-back {
    float: left;
    height: 100%;
}

.ad {
    font-size: 1.5em;
    padding: 0 0.5em 0 0.5em !important;
    background-color: black;
    color: var(--bg-color);
    display: inline;
}

.adPositionBack {
    position: absolute;
    bottom: 0%;
    left: 5%;
    margin-left: 0.35em;
}

h1 {
    font-size: 120px;
}

p {
    font-size: 18px;
}

h2 {
    padding-bottom: 10px;
    font-size: 3em;
}

@media (max-width: 507px) {
    .postcard-cover {
        margin-bottom: 50px !important;
    }
}

@media (max-width: 800px) {
    .postcard-body {
        float: left !important;
    }

    .postcard-cover {
        margin-right: 80px;
        margin-bottom: 0;
    }

}
</style>