<template>
  <div class="recipe-container">
    <div v-for="recipe in recipes" :key="recipe.id" class="recipe">
      <div style="min-height: 100vh">
        <EmojieBackground :recipe="recipe" :emojieSize='4' rowHeight="1.5em" emojiPadding="0.8em" :emojieAmount='8' />
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

      </div>

      <!--  Postcard -->
      <div>
        <h1 class="recipe-title text-span dynamic-font-size">Schicke das Rezept per Postkarte!</h1>
        <div class="postcard-paypal">
          <div class="postcard postcard-paypal-item" :style="resizedHeight">
            <Postcard :recipe='recipe' :color='titleColor' :style="resizeTransform" :name='name' :street='street'
              :zip='zipCode()' :country='country' />
          </div>
          <div class="paypal-container postcard-paypal-item">
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
              <div class="addressError" v-if='!showPaypalButton()'>❌<b>Bitte alle Felder ausfüllen!</b></div>
              <h3 class="moneyAsking">Du unterstützt uns mit:</h3>
              <span class="moneySpan">
                <div>{{price.toFixed(2)}} € + </div>
                <input class="moneyInput" type="number" :placeholder='0.50' :min='0' :step='0.5' v-model="money">
                <div>€ = <b>{{parseFloat(money) ? (price + parseFloat(money)).toFixed(2) : price.toFixed(2)}} €</b></div>
              </span>
              <h3 class="moneyAsking" v-if='showPaypalButton()'>Jetzt {{price+parseFloat(money)}}€ bezahlen:</h3>
            </div>
            <Paypal v-if='showPaypalButton()' :recipeID='recipe.id'
              :sendTo='{name: name, street: street, plz: plz, city:city, country: country}'
              :amount='price+parseFloat(money)' />
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
        scale: window.innerWidth / 1480 * 0.7
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
      }
    },
    computed: {
      resizeTransform() {
        const scale = 0.25 * (window.innerWidth - 16 * 4) / 1440
        const responsiveScale = window.innerWidth > 1100 ? scale : scale * 1.7
        return {
          "transform": "scale(" + responsiveScale + ")",
          "transform-origin": "top left"
        }
      },
      resizedHeight() {
        const scale = (1040 * 2 * ((window.innerWidth - 16 * 4) / 1440) + 100) / 3
        const responsiveScaleNextToEachOther = window.innerWidth > 1100 ? scale : scale / 1.4
        const responsiveScale = window.innerWidth > 500 ? responsiveScaleNextToEachOther :
          responsiveScaleNextToEachOther * 2;
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
  @media (max-width: 1100px) {
    .address input {
      width: 100%
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

  .postcard-paypal-item {
    float: left
  }

  .postcard {
    margin-left: 5%;
    overflow: hidden;
    width: 35%;
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
    height: 2.5em;
    padding-left: 1em;
    padding-top: 1em;
    padding-bottom: 0.3em;
    margin: 0.25em;
    text-align: center;
    color: red;
  }

  .countrySelect select {
    width: 80%;
    padding-left: 0.25em;
  }

  .address {
    padding-bottom: 6em;
    overflow: hidden;
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

    width: 48%;
    float: left;
    overflow: hidden;
    align-items: center;
    vertical-align: baseline;
    height: 2.5em
      /* margin-top: 1em */
  }

  .moneySpan div {
    margin: 0.5em;
    height: 2.5em;
    float: left;
  }

  .moneyInput {
    width: 15% !important;
    /* height:auto !important; */
    /* border: none !important; */
    padding-left: 1em;
    padding-right: 1em;
    padding-top: 0em !important;
    padding-bottom: 0em !important;
    margin: 0em !important;
    text-align: center;
  }

  .paypal-container {
    width: 60%;
    padding-top: 2.5em;
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
  }
</style>