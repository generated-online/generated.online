<template>
  <div class="recipe-container">
    <div v-if='recipe'>
      <EmojieBackground :recipe="recipe" :emojieSize='4' rowHeight="1.5em" emojiPadding="0.8em" :emojieAmount='8' />
      <div style="min-height: 100vh">
        <div class="title-container">
          <h1 class="recipe-title text-span dynamic-font-size">
            {{ recipe.title }}
          </h1>
          <Voting class="recipe-vote dynamic-font-size" :recipe='recipe' />
        </div>

        <div class="recipe-body">
          <!-- ZUTATEN -->
          <div class="ingredients text-span">
            <div class="ingredient" :key="ingredient+String(Math.floor(Math.random() * 100))" justify="center"
              v-for="ingredient in recipe.ingredients">
              <span>{{ ingredient }}</span>
            </div>
            <div class="divider"></div>
          </div>

          <!--  Instructions -->
          <span class="instruction text-span">
            {{ recipe.instructions }}
          </span>
        </div>

        <!--  Postcard -->
        <PayPalPostcard :recipe='recipe' />
      </div>
    </div>
  </div>
</template>

<script>
  import firebase from "firebase";
  import recipeToColor from "@/functions/recipe_to_color";
  import Voting from "@/components/Voting"
  import EmojieBackground from "@/components/EmojieBackground"
  import PayPalPostcard from "@/components/PayPalPostcard"

  export default {
    name: "recipe",
    components: {
      Voting,
      EmojieBackground,
      PayPalPostcard
    },
    data() {
      return {
        id: "",
        recipe: undefined,
        error: "",
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
        this.recipe = {
          id: doc.id,
          ingredients: doc.data().ingredients,
          title: doc.data().title,
          instructions: doc.data().instructions,
          votes: doc.data().votes || 0,
        };

        this.$emit('shareText', 'Schau dir dieses coole KI generierte Rezept an: ' + this.recipe['title']);
        this.$emit('recipeId', this.recipe.id);
        if (this.id === undefined) {
          this.$router.replace("/recipe/" + doc.id);
        }
      },
    }
  };
</script>

<style scoped>
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
    padding-left: 2%;
    padding-right: 2%;
    padding-top: 2%
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
      padding-bottom: 0.5em;
      width: 50%;
      float: left;
    }

    .ingredients {
      width: 100%;
      margin-bottom: 2em;
    }

    .instruction {
      float: left;
      padding: 2%;
      margin: 0 0 2em 0;
      width: 100%;
    }

    .divider {
      position: absolute;
      left: 48%;
      top: 5%;
      bottom: 60%;
      border-left: 2px solid rgb(0, 0, 0);
    }
  }

  @media (min-width: 500px) and (max-width: 600px) {
    .ingredient {
      font-size: 1em;
      padding-bottom: 0.5em;
      width: 50%;
      float: left;
    }

    .divider {
      bottom: 75%;
    }
  }

  @media (max-width: 500px) {
    .ingredient {
      font-size: 1.4em;
      padding-bottom: 0.5em;

      width: 100%;
      float: none;

    }

    .divider {
      border-left: none;
    }
  }
</style>