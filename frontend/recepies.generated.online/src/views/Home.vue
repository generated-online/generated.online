<template>
  <div class="container">

    <div v-for="recipe in recipes" :key="recipe.id" class="recipe">
      <div class="title-container" :style="'background:'+ titleColor">
        <span class="recipe-title">
          {{ recipe.title}}
        </span>
      </div>

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

      </div>

          <div class="mybutton-container">
      <button @click="$router.replace('/'); $router.go('/')">Neues Rezept generieren!</button>
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
        id: '',
        recipes: [],
        error: "",
        titleColor: ''
      }
    },
    created() {
      let db = firebase.firestore();
      const ref = db.collection("800x50")

      this.id = this.$route.params.id;
      let key = ""
      if (typeof this.id !== 'undefined') {
        ref.doc(this.id).get().then((doc) => {
          this.loadData(doc)
        })
      } else {
        key = db.collection("800x50").doc().id;
        ref
          .where(firebase.firestore.FieldPath.documentId(), '>=', key).limit(1)
          .get()
          .then(snap => {
            if (snap.size === 0) {
              ref
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
      }

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
        this.$router.replace('/' + doc.id)
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
  body,
  #app {
    margin: 0;
    padding: 0;
    overflow-x: hidden;
    max-width: 100vw !important;
    min-height: 100vh !important;
  }

  button {
    background: whites;
    margin-top: 3em;
        margin-bottom: 3em;

    padding: 0.3em 1em 0.3em 1em;
    font-size: 1.5em;
    border: none;
    cursor: grab;
    width: 100%;
    text-align: left;
  }

  .mybutton-container {
    float: left;
    width: 100%;
    /* margin: 5em 0 5em 0; */
  }

  .container {
    text-align: left;
    height: 100%;
    padding: 2em 5em 2em 5em;
    font-family: "Roboto";
  }

  .recipe-title {
    font-size: calc(70vw/15);
    padding: 0.2em 0.2em 0.2em 0.2em;
    word-wrap: break-word;
    font-family: "Commissioner";
  }

  .recipe-body {
    margin-top: calc(70vw/15);
    position: relative;
  }

  .ingredient {
    padding-left: 1em;
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

    font-size: 1.5em;
    max-width: 65vw;
    text-align: justify;
  }

  @media (max-width: 1100px) {
    .container {
      padding: 2em 2em 2em 2em !important;
    }

    .ingredients {
      float: none;
      max-width: 90vw !important;
      padding-bottom: 2em;
    }

    .recipe-title {
      font-size: calc(70vw/8) !important;
      text-align: center !important;

    }

    .title-container {
      text-align: center;
    }

    .ingredient {
      padding-bottom: 0.5em !important;
      width: 90vw !important;
      padding-left: 0 !important;
    }
    button {
      text-align: center;
    }

    .instruction {
      float: none;
      padding-left: 0 !important;
      margin: 0 !important;
      max-width: 90vh !important;

    }

  }
</style>