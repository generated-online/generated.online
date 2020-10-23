<template>
  <div class="container">
    <div v-for="recipe in recipes" :key="recipe.id" class="recipe">
      <span class="recipe-title" :style="'background:'+ titleColor">
        {{ recipe.title}}
      </span>

      <div class="recipe-body">
        <!-- ZUTATEN -->
        <div class="ingredients">
          <div class="ingredient" :key="ingredient" justify="center" v-for="ingredient in recipe.ingredients">
            {{ingredient}}
          </div>
        </div>

        <!--  Instructions -->
        <div class="instruction">
          {{recipe.instructions}}
        </div>
        <!-- Votes -->
        <!-- <div class="vote-section">
          <v-btn class="ma-5" color="transparent" fab depressed>
            <v-icon size="35" class="green-highlight">thumb_up</v-icon>
          </v-btn>
          <span class="counter large-font">
            {{recipe.counterVal}}
          </span>
          <v-btn class="ma-5" color="transparent" fab depressed>
            <v-icon size="35" class="red-highlight">thumb_down</v-icon>
          </v-btn>
        </div> -->


      </div>
    </div>
  </div>
</template>

<script>
  import firebase from "firebase";

  export default {
    name: 'home',
    components: {},
    data() {
      return {
        recipes: [],
        error: "",
        titleColor: ''
      }
    },
    created() {
      let db = firebase.firestore();
      var key = db.collection("firstTest").doc().id;
      db
        .collection("firstTest")
        .where(firebase.firestore.FieldPath.documentId(), '>=', key).limit(1)
        .get()
        .then(snap => {
          if (snap.size === 0) {
            db
              .collection("firstTest")
              .where(firebase.firestore.FieldPath.documentId(), '<', key).limit(1)
              .get()
              .then(snap => {
                snap.docs.map(this.loadData);
              })
          } else {
            snap.docs.map(this.loadData);
          }
        })
        .catch(err => {
          this.error = err
        });

    },
    methods: {
      loadData(doc) {
        this.recipes.push({
          id: doc.title,
          ingredients: doc.data().intrigents,
          title: doc.data().title,
          instructions: doc.data().instructions,
          counterVal: Math.round(Math.random() * 100)
        });
        this.pickTitleColor(doc.id)
      },
      pickTitleColor(id) {

        const colors = ["lightcoral", "lightcyan", "lightblue", "lightgoldenrodyellow", "lightgreen", "lightpink",
          "lightsalmon", "lightseagreen", "lightskyblue", "lightsteelblue", "lightyellow"
        ].sort(() => Math.random() - 0.5);
        this.titleColor = colors[0];

      }
    }
  }
</script>

<style>
  .container {
    margin: 0;
    padding: 0;
    overflow-x: hidden;
    max-width: 100vw !important;
    height: 100%;
    width: 90vw !important;
    text-align: left;
    padding: 2em 0 5em 5em;
    font-family: "Roboto";

  }

  .recipe-title {
    font-size: calc(70vw/15);
    padding: 0.2em 0.2em 0.2em 0.2em;
    word-wrap: break-word;
    font-family: "Commissioner";
  }

  .recipe-body {
    margin-top: 5em;
    position: relative;
  }

  .ingredient {
    padding-bottom: 1em;
    font-size: 1.4em;
  }

  .ingredients {
    float: left;
    width: 20vw;
  }


  .instruction {
    margin-left: 2em;
    float: left;
    font-size: 2em;
    max-width: 60vw;
  }
</style>