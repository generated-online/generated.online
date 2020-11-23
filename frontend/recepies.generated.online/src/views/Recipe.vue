<template>
  <div>
    <div class="recipe-container">
      <div v-for="recipe in recipes" :key="recipe.id" class="recipe">
        <div style="position: relative">
          <EmojieBackground :recipe="recipe" :rowHeight="'200px'"/>

          <div class="title-container">
            <span class="recipe-title text-span">
              {{ recipe.title }}
              <Voting :recipe='recipe' />
            </span>
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

        <div class="postcard" :style="resizedHeight">
          <Postcard :recipe='recipe' :color='titleColor' :style="resizeTransform" />
        </div>
        <Paypal :recipe='recipe' :color='titleColor' />

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
        id: "",
        recipes: [],
        error: "",
        titleColor: "",
        scale: window.innerWidth / 1480 * 0.7
      };
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
    },
    computed: {
      resizeTransform() {
        return {
          "transform": "scale(" + (window.innerWidth - 16 * 4) / 1440 + ")",
          "transform-origin": "top left"
        }
      },
      resizedHeight() {
        return {
          "height": 1040 * 2 * ((window.innerWidth - 16 * 4) / 1440) + 100 + "px",
          "overflow": "hidden"
        }
      }

    }
  };
</script>

<style scoped>
  .recipe-container {
    text-align: left;
    height: 100%;
    padding: 2em 0em 2em 0em;
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

  .postcard {
    overflow: hidden;
  }

  @media (max-width: 800px) {
    .recipe-container {
      padding: 2em 0em 2em 0em !important;
      /* margin: 0 0 2em 0 !important; // this breaks things! */
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