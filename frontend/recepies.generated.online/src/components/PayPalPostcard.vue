<template>
    <div>
        <h1 class="text-span dynamic-font-size">Schicke das Rezept per Postkarte!</h1>
        <div>
            <div class="postcard postcard-paypal-item" :style="resizedHeightValue">
                <Postcard :recipe='recipe' :style="resizeTransformValue" :name='name' :street='street' :zip='zipCode()'
                    :country='country' />
            </div>
            <div class="paypal-container postcard-paypal-item text-span ">
                <h1>Sichere dir eine einzigartige Rezept-Karte jetzt ab {{price.toFixed(2)}} €!</h1>
                <br>
                <h3>Die Karte geht an:</h3>
                <div class="address">
                    <input type="text" placeholder="❌ Name" v-model="name">
                    <input type="text" placeholder="❌ Straße" v-model="street">
                    <br>
                    <input type="number" placeholder="❌ Postleitzahl" v-model="plz">
                    <input type="text" placeholder="❌ Ort" v-model="city">
                    <div class="countrySelect">
                        <label for="countries">Land: </label>
                        <select name="countries" id="countries" v-model="country">
                            <option value="DE">Deutschland</option>
                            <option value="AT">Österreich</option>
                            <option value="CH">Schweiz</option>
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
                default: {}
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
            };
        },
        created() {
            window.addEventListener('resize', () => {
                this.resizeTransformValue = this.resizeTransform();
                this.resizedHeightValue = this.resizedHeight();
            })
        },
        watch: {
            money: function (newVal, oldVal) {
                newVal < 0 ? this.money = 0 : null
            }
        },
        methods: {
            showPaypalButton() {
                return this.name.length > 0 && this.street.length > 0 && this.plz > 0 && this.city.length > 0;
            },
            zipCode() {
                return !(this.plz.length + this.city.length === 0) ? this.plz + " " + this.city : ""
            },
            resizeTransform() {
                const width_percentage_of_parent = 0.33;
                const scale = width_percentage_of_parent * (window.innerWidth - 16 * 4) / 1440
                // on mobile we need to make it bigger
                var responsiveScale = window.innerWidth > 800 ? scale : scale * 1.375

                // somehow there is again a switch happening at 500 px
                if (window.innerWidth < 507) {
                    responsiveScale *= 2
                }
                return {
                    "transform": "scale(" + responsiveScale + ")",
                    "transform-origin": "top left"
                }
            },
            resizedHeight() {
                // this cuts of the hight that is produced by using the transform function to make the postcard smaller
                const scale = (1040 * 2 * ((window.innerWidth - 16 * 4) / 1440) + 200) / 3
                const responsiveScaleNextToEachOther = window.innerWidth > 800 ? scale : scale / 1.4
                const responsiveScale = window.innerWidth > 500 ? responsiveScaleNextToEachOther :
                    responsiveScaleNextToEachOther * 3.1;
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
        /* width: 65% */
    }

    .postcard {
        /* margin-left: 5%; */
        /* overflow: hidden; */
        /* float: left; */
        width: 33%;
        margin-right: 2%
    }

    .paypal-container {
        width: 63%;
        margin-left: 2%;
        /* padding-top: 2.5em; */
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
        /* width: 80%; */
        padding-left: 0.25em;
        padding-right: 0.25em;
    }

    .address {
        /* padding-bottom: 6em; */
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

    @media (max-width: 800px) {
        .dynamic-font-size {
            font-size: calc(70vw / 8);
        }

        .countrySelect,
        .address input {
            width: 100% !important;
            margin-left: 0 !important;
            margin-right: 0 !important;
        }

        .postcard-body {
            float: none !important;
        }

        .postcard {
            width: 100% !important
        }

        .paypal-container {
            width: 100% !important
        }
    }
</style>