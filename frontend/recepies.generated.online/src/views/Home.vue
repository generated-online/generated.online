<template>
  <v-content>
    <div class="home" color="primary">
      <!-- RECIPE CONTAINER-->
      <v-container>
        <v-card v-for="recipe in recipes" :key="recipes.id" class="pa-5 ma-5" color="error--text">
          <v-card-title class="large-font text-center justify-center">
            {{recipe.title}}
          </v-card-title>
          <v-divider/>
          <v-container fluid>
            <v-row>
              <v-col cols="12">
                <v-row align="center" justify="center">
                  <v-content key="1" class="half">
                    <v-img src="https://picsum.photos/510/300?food" align="center" justify="center"></v-img>
                  </v-content>
                  <v-content key="0" class="half">
                    <v-list class="list">
                      <v-list-item class="list normal-font" align="center" justify="center" v-for="ingredient in recipe.ingredients">{{ingredient}}</v-list-item>
                    </v-list>
                  </v-content>
                </v-row>
              </v-col>
            </v-row>
          </v-container>
          <v-divider/>

          <v-container>
            <v-card-text class="text-justify larger-font">
              {{recipe.instructions}}
            </v-card-text>
          </v-container>

          <v-container class="">
            <v-btn class="ma-5" color="transparent" fab depressed>
              <v-icon size="35" class="green-highlight">thumb_up</v-icon>
            </v-btn>
            <span class="counter large-font">
              {{recipe.counterVal}}
            </span>
            <v-btn class="ma-5" color="transparent" fab depressed>
              <v-icon size="35" class="red-highlight">thumb_down</v-icon>
            </v-btn>
          </v-container>
        </v-card>
      </v-container>
    </div>
  </v-content>
</template>

<script>
import firebase from "firebase";

export default {
  name: 'home',
  components: {
  },
  data() {
    return {
      recipes: [],
    }
  },
  created() {
    let db = firebase.firestore();
    let potholeRef = db
            .collection("firstTest")
            .get()
            .then(snap => {
              snap.docs.map(doc => {
                if (doc.data().title !== '') {
                  this.recipes.push({
                    id: doc.title,
                    ingredients: doc.data().intrigents,
                    title: doc.data().title,
                    instructions: doc.data().instructions,
                    // TODO: ADD REAL COUNTER
                    counterVal: Math.round(Math.random()*100)
                  });
              }
              });
            })
            .catch(err => {
              console.log('Error getting document', err)
            });
  },
  methods: {
    updateX: function() {

    }
  }
}
</script>

<style>
  .counter {
    line-height: 2.5em !important;
    position:relative;
    top:10px
  }
  @media only screen and (min-width: 900px) {
    .half {
    width: 50%;
    }
  }
  .item {
    align-content: ;
    margin: 1em;
    padding: 1em;
    text-decoration: none;
    font-size: 2em;
    border-style: groove;
    border-radius: 100px;
    border-color: black;
    color: black;
    display: inline-block;
    transition: 0.5s;
  }
  .item:hover {
    background: #5c6bc0;
    color: #ECEFF1;
  }

  li img {
    width: 32px;
    bottom: 0;
    vertical-align:middle
  }
  a:visited {
    color: black
  }
</style>
