<template>
    <div
        :style="'transform: scale(' + scaling()+'); transform-origin: top left; width: '+(horizontal?'max-content':'min-content')+'; height: '+height+'px'" id="postcard">
        <div class="postcard-body" id="postcard-front"
            :style="{'margin-bottom': horizontal ? 0 : bottomMargin, 'margin-right': horizontal ? centerMargin : 0, 'float':'left'}">
            <EmojieBackground :recipe="recipe" :opacity="1" color="var(--bg-color)" class="background now-color"/>
            <div class="postcard-inner">
                <div :style="'line-height: 1.3em; font-size:' + titleSize" >
                    <span v-for="titlePart in recipe.title.split(' ')" class="clip-text" :key="titlePart">{{titlePart}} </span>
                </div>
                <div class="ad adPositionFront clip-text mt-4 px-2"> recipes.generated.online </div>
            </div>
        </div>
        <div class="postcard-body" id="postcard-back" :style="{'background':'white', 'float': horizontal?'right':'left'}">
            <div>
                <div class="half-postcard" >
                    <h2>{{ recipe.title }}</h2>
                    <p v-for="(ingredient, n) in recipe.ingredients" :key="n"
                        :style="'font-size:'+ instructionSize">{{ ingredient }}</p>
                    <br>
                    <p :style="'text-align: justify;font-size:'+ instructionSize">{{ recipe.instructions }}</p>
                    <br>
                    
                    <p v-show="grussZeile" class="ad">{{grussZeile}}</p>

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
                <p class="ad adPositionBack clip-text px-2" style="background: black">{{absender? 'gesendet von '+ absender + ' via ':''}}recipes.generated.online</p>
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
            "absender":{
              type:String,
              default: ""
            },
            "grussZeile":{
              type:String,
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
                "titleSize": "8em",
                "instructionSize": "1em",
                "bottomMargin": "4em",
                "centerMargin": "4em",
                height: 100
            }
        },
        components: {
            EmojieBackground,
        },
        created() {
            if (this.recipe.title.length > 100) {
                this.titleSize = "6em"
            } else if (this.recipe.title.length > 70) {
                this.titleSize = "7em"
            }
            // else standard applies

            // get approximate line number, about 25 lines fit on the card
            const lines = this.recipe.instructions.length / 100 + this.recipe.ingredients.length
            if (lines > 33) {
                this.instructionSize = "0.6em"
            } else if (lines > 31) {
                this.instructionSize = "0.7em"
            } else if (lines > 29) {
                this.instructionSize = "0.8em"
            } else if (lines > 27) {
                this.instructionSize = "0.9em"
            } else if (lines > 25) {
                this.instructionSize = "1em"
            } else if (lines > 23) {
                this.instructionSize = "1.1em"
            } else if (lines > 21) {
                this.instructionSize = "1.2em"
            } else if (lines > 19) {
                this.instructionSize = "1.3em"
            } else if (lines > 17) {
                this.instructionSize = "1.4em"
            } else if (lines > 15) {
                this.instructionSize = "1.5em"
            } else if (lines <= 15) {
                this.instructionSize = "1.6em"
            }
            // else standard applies
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
                let height = this.scaledHeight(scaleFactor)
                this.$emit("height", height)

                this.height = height / scaleFactor

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

<style lang="scss" scoped>
    $textBGColor: black;
    /*rgba(0, 0, 0, 0.8);*/

    .clip-text {
        color: var(--bg-color);
        background: $textBGColor;
        box-decoration-break: clone;
        -webkit-box-decoration-break: clone;
    }

    .stamp {
        position: absolute;
        width: 145px;
        height: 190px;
        border: dashed black 2px;
        background: whitesmoke;
        right: 4%;
    }

    input:disabled {
        color: black;
    }

    input {
        padding-top: 10px;
        margin-top: 10px;
        width: 70%;
        margin-right: 20%;
        margin-left: 10%;
        background: whitesmoke;
        float: right;
        display: block;
        font-size: 2em;
        padding-left: 1em;
    }

    .address {
        border-left: solid black 4px;
        position: absolute;
        top: 300px;
        padding-top: 150px;
        left: 0;
    }

    input::placeholder {
        color: rgb(170, 170, 170) !important;
    }

    .half-postcard {
        color: black !important;
        position: relative;
        width: 50%;
        float: left;
        height: 100%;
        padding: 2%;
    }


    .postcard-body {
        position: relative;
        width: 1440px;
        height: 1040px;
    }

    .postcard-inner {
        padding-left: 140px;
        padding-top: 124px;
        padding-right: 70px;
        height: 100%;
    }

    .ad {
        font-size: 1.5em;
        padding: 0.25em 0 0.25em 0;
        font-weight: bold;
    }

    .adPositionFront {
      width: fit-content;
      height: fit-content;
    }

    .adPositionBack {
        position: absolute;
        bottom: 0;
        left: 2.5%;
        margin-left: 0.35em;
    }

    p {
        font-size: 18px;
        margin: 0 !important;
        padding: 0 !important
    }

    h2 {
        padding-bottom: 10px;
        font-size: 3em;
    }
</style>