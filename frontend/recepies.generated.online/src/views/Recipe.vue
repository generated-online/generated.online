<template>
  <div class="recipe-container">
    <div v-for="recipe in recipes" :key="recipe.id" class="recipe">
      <div class="title-container" :style="'background:' + titleColor">
        <span class="recipe-title">
          {{ recipe.title }}
        </span>
      </div>

      <div class="recipe-body">
        <!-- ZUTATEN -->
        <div class="ingredients">
          <div class="ingredient" :key="ingredient" justify="center" v-for="ingredient in recipe.ingredients">
            {{ ingredient }}
          </div>
        </div>

        <!--  Instructions -->
        <div class="instruction">
          {{ recipe.instructions }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import firebase from "firebase";

  export default {
    name: "recipe",
    data() {
      return {
        id: "",
        recipes: [],
        error: "",
        titleColor: "",
      };
    },
    created() {
      let db = firebase.firestore();
      const ref = db.collection("algolia-test")

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
          counterVal: Math.round(Math.random() * 100),
        });

        this.$emit('shareText', 'Schau dir dieses coole KI generierte Rezept an: ' + this.recipes[0]['title']);
        this.pickTitleColor(doc.id);
        if (this.id === undefined) {
          this.$router.replace("/recipe/" + doc.id);
        }
      },
      pickTitleColor(id) {
        const colors = [
          "lightcoral",
          "lightcyan",
          "lightblue",
          "lightgoldenrodyellow",
          "lightgreen",
          "lightpink",
          "lightsalmon",
          "lightseagreen",
          "lightskyblue",
          "lightsteelblue",
          "lightyellow",
        ].sort(() => Math.random() - 0.5);
        this.titleColor = colors[0];
      },
    },
  };
</script>

<style scoped>
  .recipe-container {
    text-align: left;
    height: 100%;
    padding: 2em 2em 2em 2em;
    min-height: 100vh;
    margin: 0 0 100px 0;
  }

  .recipe-title {
    font-size: calc(70vw / 15);
    padding: 0.2em 0.2em 0.2em 0.2em;
    word-wrap: break-word;
    font-family: "Commissioner";
  }

  .recipe-body {
    margin-top: calc(70vw / 15);
    position: relative;
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
  }


  @media (max-width: 800px) {
    .recipe-container {
      padding: 2em 2em 2em 2em !important;
      margin: 0 0 2em 0 !important;
    }

    .ingredients {
      float: none;
      width: 100% !important;
      padding-bottom: 2em;
    }

    .recipe-title {
      font-size: calc(70vw / 8) !important;
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

    .instruction {
      float: none !important;
      padding-left: 0 !important;
      margin: 0 0 2em 0 !important;
      width: 100% !important;
    }
  }
</style>