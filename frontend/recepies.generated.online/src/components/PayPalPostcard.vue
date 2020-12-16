<template>
  <div class="boldy">
    <div :class="['text-sm-h3', 'text-md-h2', 'text-h3', 'text-span' , 'font-weight-black', 'boldy']"
      style="margin-bottom: 0.5em">
      Verschicke das Rezept als Postkarte!
    </div>
    <v-container class="pb-6">
      <v-row no-gutters>
        <v-col ref="postcardCol" :style="'height: ' +postcardHeight+'px; overflow: hidden'" cols="12" lg="6" md="6">
          <!-- Postcards -->
          <Postcard ref="postcard" :absender='absender' :country='country' :horizontal="$vuetify.breakpoint.smOnly"
            :name='name' :parent-width="postcardWidth" :recipe='recipe' :street='street' :zip='zipCode()'
            @height="postcardHeight=$event" />
        </v-col>
        <v-col :style="{
                                'margin-left': $vuetify.breakpoint.mdAndUp? '2em': '0',
                                'margin-top': !$vuetify.breakpoint.mdAndUp? '2em': '0'
                                }">
          <!--  PayPal stuff -->
          <div class="center-button">
            <v-btn v-if='!showMore && $vuetify.breakpoint.xsOnly' class="black-button" @click="showMore=!showMore">
              Erfahre mehr
            </v-btn>
          </div>
          <div v-if='showMore || !$vuetify.breakpoint.xsOnly'>
            <div class="address boldy-border mb-5">
              <h2>Die Karte geht an:</h2>
              <div class="pt-3">
                <input v-model="name" class="shady" placeholder="❌ Name" type="text" maxlength="16">
                <input v-model="street" class="shady" placeholder="❌ Straße" type="text">
                <br>
                <input v-model.number="plz" class="shady" placeholder="❌ Postleitzahl" type="number">
                <input v-model="city" class="shady" placeholder="❌ Ort" type="text">
                <div class="countrySelect shady">
                  <label for="countries">Land: </label>
                  <select id="countries" v-model="country" name="countries">
                    <option value="DE">Deutschland</option>
                    <option value="AT">Österreich</option>
                    <option value="CH">Schweiz</option>
                  </select>
                </div>

              </div>
            </div>
            <v-row class="boldy-border ma-0 mb-5" cols="12">
              <v-col class="pa-0 mr-3" cols="12" lg="auto" md="12" sm="auto">
                <h2>Gesendet von: </h2>
              </v-col>
              <v-col class="pa-0">
                <input v-model="absender" class="shady nameInput ma-0" maxlength="16" placeholder="❌ Absender"
                  type="text">
              </v-col>
            </v-row>

            <v-container class="moneyAsking mb-3 boldy-border">
              <h2 class="mb-2"> Wieviel willst du zahlen?</h2>
              <div class="moneySpan mb-4">
                <div>{{ price.toFixed(2) }} € +</div>
                <div class="mx-1" style="width: min-content">
                  <input v-model.number="money" :min='0' :step='0.5' class="moneyInput ma-0 boldy-color" placeholder='0' type="number">
                </div>
                <div>€ = {{ (money > 0) ? (price + money).toFixed(2) : price.toFixed(2) }} €</div>
              </div>
              <MoneyBar :money="securedMoney" :price="price" />
            </v-container>

            <v-container class="boldy-border my-5 address">
              <h2 class="mb-4">
                Jetzt für
                {{ (price + money).toFixed(2) }}€
                kaufen!
              </h2>
              <Paypal :amount='price+securedMoney' :recipeID='recipe.id'
                :sendTo='{name: name, street: street, plz: plz, city:city, country: country, absender:absender}'
                style="text-align: center" />
            </v-container>
            <div v-if="$vuetify.breakpoint.xs" class="center-button" style="margin-top: 1em">
              <v-btn class="black-button" @click="showMore=!showMore">Weniger</v-btn>
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
        absender: '',
        price: 3.50,
        money: 0.5,
        securedMoney: 0.5,
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
        if (newVal < 0 || (typeof newVal === "string")) {
          this.money = null
          this.securedMoney = 0
        } else {
          this.securedMoney = newVal
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


<style lang="scss" scoped>
  h3 {
    padding-bottom: 1em;
  }

  .countrySelect,
  .moneyInput,
  .nameInput,
  .address input {
    padding-left: 1em;
    padding-top: 0.3em;
    padding-bottom: 0.3em;
    background: var(--bg-color);
    color: black;
  }

  .nameInput {
    width: 100%
  }

  .countrySelect,
  .moneyInput,
  .address input {
    margin: 1%;
    width: 48%;
    float: left;
  }


  .addressError {
    float: left;
    width: 100%;
    padding: 0.5em;
    text-align: center;
    margin-top: 1em;
  }

  .countrySelect select {
    padding-left: 0.25em;
    padding-right: 0.25em;
    color: black;
  }

  .address {
    overflow: auto;
  }

  .moneyAsking {
    width: 100%;
    float: left;
  }

  .moneySpan {
    font-weight: bold;
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

  input::placeholder {
    color: rgba(0, 0, 0, 0.5) !important;
  }

  .center-button {
    width: 100%;
    text-align: center
  }

  .center-button {
    width: 100%;
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