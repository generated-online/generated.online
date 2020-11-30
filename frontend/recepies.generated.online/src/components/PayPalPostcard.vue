<template>
    <div>
        <h1 class="text-span dynamic-font-size" style="margin-bottom:0.5em">
            Verschicke das Rezept als Postkarte!</h1>
        <div>
            <div class="postcard postcard-paypal-item" :style="resizedHeightValue">
                <Postcard :recipe='recipe' :style="resizeTransformValue" :name='name' :street='street' :zip='zipCode()'
                    :country='country' />
            </div>
            <div class="center-button">
                <v-btn v-if='!showMore && showButtons' @click="showMore=!showMore" class="black-button">Erfahre mehr
                </v-btn>
            </div>
            <div v-if='showMore || !showButtons' class="paypal-container postcard-paypal-item text-span ">
                <h1>Sichere dir eine einzigartige Rezept-Karte jetzt ab {{price.toFixed(2)}} €!</h1>
                <br>
                <h3>Die Karte geht an:</h3>
                <div class="address">
                    <input type="text" placeholder="❌ Name" v-model="name">
                    <input type="text" placeholder="❌ Straße" v-model="street">
                    <br>
                    <input type="number" placeholder="❌ Postleitzahl" v-model.number="plz">
                    <input type="text" placeholder="❌ Ort" v-model="city">
                    <div class="countrySelect">
                        <label for="countries">Land: </label>
                        <select name="countries" id="countries" v-model="country">
                            <option scaling_factor="DE">Deutschland</option>
                            <option scaling_factor="AT">Österreich</option>
                            <option scaling_factor="CH">Schweiz</option>
                        </select>
                    </div>
                    <br>
                    <div class="addressError" v-if='!showPaypalButton()'>
                        <div> ❌<b>Bitte alle Felder
                                ausfüllen!</b></div>

                    </div>
                    <h3 class="moneyAsking">Du unterstützt uns mit:</h3>
                    <div class="moneySpan">
                        <div>{{price.toFixed(2)}} € + </div>
                        <div class="ml-1" style="width: min-content">
                            <input class="moneyInput" type="number" :min='0' :step='0.5' v-model.number="money">
                        </div>
                        <div>€ <b> = {{money ? (price + money).toFixed(2) : price.toFixed(2)}} €</b></div>
                    </div>
                    <h3 class="moneyAsking" v-if='showPaypalButton()'>Jetzt {{(price+money).toFixed(2)}}€ bezahlen:</h3>
                </div>
                <Paypal v-if='showPaypalButton()' :recipeID='recipe.id'
                    :sendTo='{name: name, street: street, plz: plz, city:city, country: country}'
                    :amount='price+money' />
                <div v-if="showButtons" class="center-button" style="margin-top: 1em">
                    <v-btn @click="showMore=!showMore" class="black-button">Weniger</v-btn>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Postcard from "@/components/Postcard"
    import Paypal from "@/components/Paypal"
    import EmojieBackground from "@/components/EmojieBackground"
    export default {
        components: {
            Postcard,
            EmojieBackground,
            Paypal,
        },
        props: {
            "recipe": {
                type: Object,
                default: undefined
            },
        },
        data() {
            return {
                name: '',
                street: '',
                plz: '',
                city: '',
                country: 'DE',
                price: 3.50,
                money: 0.5,
                resizeTransformValue: this.resizeTransform(),
                resizedHeightValue: this.resizedHeight(),
                showMore: false,
                showButtons: window.innerWidth < 800
            };
        },
        created() {
            window.addEventListener('resize', () => {
                this.resizeTransformValue = this.resizeTransform();
                this.resizedHeightValue = this.resizedHeight();
                this.showButtons = window.innerWidth < 800;
            })
        },
        watch: {
            money: function (newVal, oldVal) {
                newVal < 0 ? this.money = 0 : null
            },
            showMore: function (newVal, oldVal) {
                if (newVal) {
                    // need timeout otherwise the size is not changed yet :/
                    setTimeout(() => {
                        window.dispatchEvent(new Event('resize'))
                    }, 10);
                }
            }
        },
        methods: {
            showPaypalButton() {
                return this.name.length > 0 && this.street.length > 0 && this.plz > 0 && this.city.length > 0;
            },
            zipCode() {
                return !(this.plz.length + this.city.length === 0) ? this.plz + " " + this.city : ""
            },
            calculatePostcardScalingFactor() {
                // one postcards size is:
                // [0-506]      100% - 4em
                // [507 - 800]  (100% - 4em) / 2 (be sure of the space between them)
                // [801 -> ]    (100% - 4em) / 3

                var em = parseFloat(getComputedStyle(this.$parent.$el).fontSize);

                // this is the percentage of the space the postcards should take
                var width_percentage_of_parent = 0;

                // this is the space between both postcards (80 when next to each other)
                var postcard_margin = 0;

                var curr_width = window.innerWidth;

                if (curr_width < 507) {
                    width_percentage_of_parent = 1.
                } else if (curr_width < 801) {
                    width_percentage_of_parent = 0.5
                    postcard_margin = 80;
                } else {
                    width_percentage_of_parent = 0.33
                }

                var padding_in_width_direction = 4 * em;

                var postcard_width = 1440;

                var scale = width_percentage_of_parent * (window.innerWidth - padding_in_width_direction) / (
                    postcard_width +
                    postcard_margin / 2)
                return scale
            },
            resizeTransform() {
                return {
                    "transform": "scale(" + this.calculatePostcardScalingFactor() + ")",
                    "transform-origin": "top left"
                }
            },
            resizedHeight() {

                var scaling_factor = this.calculatePostcardScalingFactor();
                // when the postcards are above each other this will be set to 2 -> double the height
                var heightMultiplier = 1;
                // this is the space between both postcards when above each other
                var postcard_margin = 0;

                var curr_width = window.innerWidth;

                // postcards are only above each other in these ranges
                if (curr_width < 507 || curr_width > 800) {
                    heightMultiplier = 2.
                    postcard_margin = 50;
                }

                var postcard_height = 1040;

                var responsiveScale = scaling_factor * (postcard_height * heightMultiplier + postcard_margin);
                return {
                    "height": responsiveScale + "px",
                    "overflow": "hidden"
                }
            }
        }
    }
</script>


<style scoped>
    h3 {
        padding-bottom: 1em;
    }

    .postcard-paypal-item {
        float: left;
    }

    .postcard {
        width: 33%;
        margin-right: 2%;
        margin-bottom: 1.5em;
    }

    .paypal-container {
        width: 65%;
        padding: 1em;
    }

    .countrySelect,
    .address input {
        width: 48%;
        float: left;
        height: 2.5em;
        border: 2px dashed black;
        padding-left: 1em;
        padding-top: 0.3em;
        padding-bottom: 0.3em;
        margin: 0.25em;
    }

    .addressError {
        float: left;
        width: 100%;
        padding: 0.5em;
        text-align: center;
        color: red;
        background: black;
        margin-top: 1em;
    }

    .countrySelect select {
        padding-left: 0.25em;
        padding-right: 0.25em;
    }

    .address {
        overflow: auto;
    }

    .moneyAsking {
        width: 100%;
        float: left;
        margin-top: 1em
    }

    .moneySpan {
        width: 100%;
        float: left;
        overflow: visible;
    }

    .moneySpan div {
        display: inline-flex;
    }

    .moneyInput {
        min-width: 4em;
        padding: 0 !important;
        margin: 0 !important;
        text-align: center;
    }

    /* hide arrows in number input field */
    input::-webkit-outer-spin-button,
    input::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }

    input[type=number] {
        -moz-appearance: textfield;
    }

    .dynamic-font-size {
        font-size: calc(70vw / 15);
        font-family: "Commissioner";
        padding: 0.2em 0.2em 0.2em 0.2em;
    }

    .recipe-title {
        word-wrap: break-word;
        width: 80%;
        display: inline-block;
    }

    .center-button {
        width: 100%;
        /* float: left; */
        text-align: center
    }

    @media (max-width: 507px) {

        .countrySelect,
        .address input {
            width: 100% !important;
            margin-left: 0 !important;
            margin-right: 0 !important;
        }
    }

    @media (max-width: 800px) {
        .dynamic-font-size {
            font-size: calc(70vw / 8);
        }

        .postcard {
            width: 100% !important;
        }

        .paypal-container {
            width: 100% !important;
            margin: 0 !important
        }

    }
</style>