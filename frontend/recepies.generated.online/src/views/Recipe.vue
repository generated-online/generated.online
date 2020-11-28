<template>
  <div class="recipe-container">
    <EmojieBackground v-if='recipes.length != 0' :recipe="recipes[0]" :emojieSize='4' rowHeight="1.5em"
      emojiPadding="0.8em" :emojieAmount='8' />

    <div v-for="recipe in recipes" :key="recipe.id" class="recipe">
      <div style="min-height: 100vh">
        <div class="title-container">
          <h1 class="recipe-title text-span dynamic-font-size">
            {{ recipe.title }}
          </h1>
          <Voting class="recipe-vote dynamic-font-size" :recipe='recipe' />
        </div>

        <div class="recipe-body">
          <!-- ZUTATEN -->
          <div class="ingredients">
            <div class="ingredient" :key="ingredient+String(Math.floor(Math.random() * 100))" justify="center"
              v-for="ingredient in recipe.ingredients">
              <span class="text-span">{{ ingredient }}</span>
            </div>
          </div>

          <!--  Instructions -->
          <span class="instruction text-span">
            {{ recipe.instructions }}
          </span>
        </div>

        <!--  Postcard -->
        <div>
          <h1 class="text-span dynamic-font-size">Schicke das Rezept per Postkarte!</h1>
          <div>
            <div class="postcard postcard-paypal-item" :style="resizedHeightValue">
              <Postcard :recipe='recipe' :color='titleColor' :style="resizeTransformValue" :name='name' :street='street'
                :zip='zipCode()' :country='country' />
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
                :sendTo='{name: name, street: street, plz: plz, city:city, country: country}' :amount='price+money' />
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
  import firebase from "firebase";
  import recipeToColor from "@/functions/recipe_to_color";
  import Voting from "@/components/Voting"
  import Postcard from "@/components/Postcard"
  import Paypal from "@/components/Paypal"
  import EmojieBackground from "@/components/EmojieBackground"

  export default {
    name: "recipe",
    components: {
      Voting,
      Postcard,
      EmojieBackground,
      Paypal
    },
    data() {
      return {
        name: '',
        street: '',
        plz: '',
        city: '',
        country: 'DE',
        id: "",
        recipes: [],
        error: "",
        titleColor: "",
        price: 3.50,
        money: 0.5,
        resizeTransformValue: this.resizeTransform(),
        resizedHeightValue: this.resizedHeight(),
      };
    },
    watch: {
      money: function (newVal, oldVal) {
        newVal < 0 ? this.money = 0 : null
      }
    },
    created() {
      let db = firebase.firestore();
      const ref = db.collection("recipes")

      this.id = this.$route.params.id;
      let key = "";
      if (typeof this.id !== "undefined") {
        ref
          .doc(this.id)
          .get()
          .then((doc) => {
            this.loadData(doc);
          });
      } else {
        key = ref.doc().id;
        ref
          .where(firebase.firestore.FieldPath.documentId(), ">=", key)
          .limit(1)
          .get()
          .then((snap) => {
            if (snap.size === 0) {
              ref
                .where(firebase.firestore.FieldPath.documentId(), "<", key)
                .limit(1)
                .get()
                .then((snap) => {
                  snap.docs.map(this.loadData);
                });
            } else {
              snap.docs.map(this.loadData);
            }
          })
          .catch((err) => {
            this.error = err;
          });
      }
      window.addEventListener('resize', () => {
        this.resizeTransformValue = this.resizeTransform();
        this.resizedHeightValue = this.resizedHeight();
      })
    },
    methods: {
      loadData(doc) {
        this.recipes.push({
          id: doc.id,
          ingredients: doc.data().ingredients,
          title: doc.data().title,
          instructions: doc.data().instructions,
          votes: doc.data().votes || 0,
        });

        this.$emit('shareText', 'Schau dir dieses coole KI generierte Rezept an: ' + this.recipes[0]['title']);
        this.$emit('recipeId', this.recipes[0].id);
        this.titleColor = recipeToColor(doc.id);
        if (this.id === undefined) {
          this.$router.replace("/recipe/" + doc.id);
        }
      },
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
        console.log("new scale: " + responsiveScale);
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
  };
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

  .inline {
    display: inline;
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

  .recipe-container {
    text-align: left;
    height: 100%;
    padding: 2em 2em 2em 2em;
    margin-bottom: 2em;
  }

  .title-container {
    position: relative;
    width: 100%
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

  .recipe-vote {
    position: absolute;
    right: 0;
    width: 300px;
  }

  .recipe-body {
    margin-top: calc(70vw / 15);
    position: relative;
    overflow: hidden;
  }

  .ingredient {
    padding-bottom: 1em;
    font-size: 1.4em;
  }

  .ingredients {
    float: left;
    width: 25%;
    margin-left: 2%;
    margin-right: 2%
  }

  .instruction {
    margin-left: 2%;
    margin-right: 2%;
    float: right;
    font-size: 1.5em;
    /* this should be exactly the space left */
    width: calc(100% - 25% - 2%*4);
    text-align: justify;
    display: block
  }

  @media (max-width: 800px) {
    .dynamic-font-size {
      font-size: calc(70vw / 8);
    }

    .ingredients {
      float: none;
      width: 100% !important;
      padding-bottom: 2em;
    }

    .recipe-title {
      text-align: center !important;
    }

    .recipe-vote {
      position: relative;
      display: inline-table;
      width: 100%;
      text-align: center;
      align-items: center;
    }

    .title-container {
      text-align: center;
    }

    .ingredient {
      padding-bottom: 0.5em !important;
      width: 90vw !important;
      padding-left: 0 !important;
    }

    .instruction {
      float: none !important;
      padding-left: 0 !important;
      margin: 0 0 2em 0 !important;
      width: 100% !important;
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