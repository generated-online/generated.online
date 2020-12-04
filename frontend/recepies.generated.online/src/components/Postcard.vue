<template>
    <div :style="'transform: scale(' + scaling()+'); transform-origin: top left; width: '+(horizontal?'max-content':'min-content')">
        <div class="postcard-body"
             :style="{'margin-bottom': horizontal?0:bottomMargin, 'margin-right': horizontal?centerMargin:0, 'float':'left'}">
            <EmojieBackground :recipe="recipe" :opacity="1" color="var(--bg-color)"/>
            <div class="postcard-inner">
                <h1>
                    <span>
                        {{ recipe.title }}
                    </span>
                </h1>
                <span class="ad">gesendet mit recipes.generated.online</span>
            </div>
        </div>

        <div class="postcard-body" :style="{'background':'white', 'float': horizontal?'right':'left'}">
            <div>
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
            default: false
        },
        "parentWidth": {
            type: Number,
            default: 100.
        }

    },
    data() {
        return {
            "bottomMargin": "2em",
            "centerMargin": "2em"
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
            } else {
                let em = 16;
                scaleFactor = this.parentWidth / ((1440) * 2 + parseFloat(this.centerMargin) * em)
            }

            this.$emit("height", this.scaledHeight(scaleFactor))
            return scaleFactor
        },
        scaledHeight(scaleFactor) {
            let bottomMargin = 0;

            if (this.$parent.$el) {
                var em = parseFloat(getComputedStyle(this.$parent.$el).fontSize);
                bottomMargin = (this.horizontal ? 0 : (parseFloat(this.bottomMargin) * em))
            }
            return scaleFactor * (1040 * (this.horizontal ? 1 : 2) + bottomMargin)
        }
    }
}
</script>

<style scoped>

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

input {
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


.postcard-body {
    position: relative;
    border: solid black 40px;
    width: 1440px;
    height: 1040px;
}

.postcard-inner {
    padding: 140px;
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
    bottom: 0;
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
</style>