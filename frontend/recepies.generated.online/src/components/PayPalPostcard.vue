<template>
    <div>
        <div :class="['text-sm-h3', 'text-md-h2', 'text-h3', 'text-span' , 'font-weight-black']"
             style="margin-bottom: 0.5em">
            Verschicke das Rezept als Postkarte!
        </div>
        <v-container class="pb-6">
            <v-row
                    no-gutters
            >
                <v-col cols="12"  md="4" lg="4" ref="postcardCol" :style="'height: ' +postcardHeight+'px'">
                    <!-- Postcards -->
                    <Postcard :recipe='recipe'
                              :name='name'
                              :street='street'
                              :zip='zipCode()'
                              :country='country'
                              :parent-width="postcardWidth"
                              :horizontal="$vuetify.breakpoint.smOnly"
                              ref="postcard"
                              @height="postcardHeight=$event"
                    />
                </v-col>
                <v-col>
                    <!--  PayPal stuff -->
                    <div class="center-button">
                        <v-btn v-if='!showMore && $vuetify.breakpoint.xsOnly' @click="showMore=!showMore"
                               class="black-button">Erfahre mehr
                        </v-btn>
                    </div>
                    <div v-if='showMore || !$vuetify.breakpoint.xsOnly' text-span>
                        <h1>Sichere dir eine einzigartige Rezept-Karte jetzt ab {{ price.toFixed(2) }} €!</h1>
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
                                    <option value="DE">Deutschland</option>
                                    <option value="AT">Österreich</option>
                                    <option value="CH">Schweiz</option>
                                </select>
                            </div>
                            <br>
                            <div class="addressError" v-if='!showPaypalButton()'>
                                <div> ❌<b>Bitte alle Felder ausfüllen!</b></div>
                            </div>
                            <h3 class="moneyAsking">Du unterstützt uns mit:</h3>


                            <div class="moneySpan">
                                <div>{{ price.toFixed(2) }} € +</div>
                                <div class="ml-1" style="width: min-content">
                                    <input class="moneyInput" type="number" :min='0' :step='0.5' v-model.number="money">
                                </div>
                                <div>€ <b> = {{ money ? (price + money).toFixed(2) : price.toFixed(2) }} €</b></div>

                                <MoneyBar :money="money" :price="price"/>
                            </div>
                            <h3 class="moneyAsking" v-if='showPaypalButton()'>Jetzt {{ (price + money).toFixed(2) }}€
                                bezahlen:</h3>
                        </div>

                        <Paypal v-if='showPaypalButton()' :recipeID='recipe.id'
                                :sendTo='{name: name, street: street, plz: plz, city:city, country: country}'
                                :amount='price+money'/>
                        <div v-if="$vuetify.breakpoint.xs" class="center-button" style="margin-top: 1em">
                            <v-btn @click="showMore=!showMore" class="black-button">Weniger</v-btn>
                        </div>
                    </div>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
import Postcard from "@/components/Postcard"
import Paypal from "@/components/Paypal"
import MoneyBar from "@/components/MoneyBar";

export default {
    components: {
        MoneyBar,
        Postcard,
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
            showMore: false,
            postcardWidth: this.calculatePostcardWidth(),
            postcardHeight: 100
        };
    },
    created() {
        window.addEventListener('resize', () => {
            this.postcardWidth = this.calculatePostcardWidth();
        })
    },
    mounted() {
        this.postcardWidth = this.calculatePostcardWidth();
    },
    watch: {
        money: function (newVal) {
            newVal < 0 ? this.money = 0 : null
        },
        showMore: function (newVal) {
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
        calculatePostcardWidth() {
            if ("postcardCol" in this.$refs) {
                return this.$refs.postcardCol.clientWidth
            } else {
                return 100.
            }
        }
    }
}
</script>


<style scoped>

input::placeholder {
    color: black
}

h3 {
    padding-bottom: 1em;
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

.address input::placeholder {
    color: rgba(1, 1, 1, .8) !important;
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
</style>