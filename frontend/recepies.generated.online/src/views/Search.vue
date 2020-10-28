<template>
  <div>
    <ais-instant-search :search-client="searchClient" index-name="Recipes">

      <ais-search-box />

      <ais-hits class="ais-hits">

        <router-link slot="item" slot-scope="{ item }" :style="'background-color:'+recipeToColor(item.objectID)"
          class="search-item" :to="'/recipe/' + item.objectID">
          <ais-highlight attribute="title" :hit="item" />
          <div>
            <span class="search-item-ingredients" v-for="ingredient in item.ingredients"
              :key="ingredient">{{ingredient}}</span>
          </div>
        </router-link>
      </ais-hits>

      <ais-state-results>
        <template slot-scope="{ state: { query }, results: { hits, nbPages } }">
          <!-- show no result if query with no hits -->
          <div v-if="query && hits.length == 0" style="text-align:center; padding: 2em 0 0 0">Keine Treffer!</div>

          <!-- hide pagination if 1 or less pages -->
          <ais-pagination v-if="nbPages > 1" />
          <div v-if="hits.length == 0" style="text-align:center; padding: 2em 0 0 0">
            <generateRecipeButton />
          </div>
        </template>
      </ais-state-results>

    </ais-instant-search>
  </div>
</template>

<script>
  import algoliasearch from 'algoliasearch/lite'
  import 'instantsearch.css/themes/algolia-min.css'
  import recipeToColor from "@/functions/recipe_to_color";
  import generateRecipeButton from "@/components/generateRecipeButton";

  const algoliaClient = algoliasearch(
    '7KL69V3MEL', // Application ID
    '6facf15b54148bc84e399e2994885c15' // Search-Only API Key
  )

  // this setup is required to prevent search on empty query
  const searchClient = {
    search(requests) {
      if (requests.every(({
          params
        }) => !params.query)) {
        return Promise.resolve({
          results: requests.map(() => ({
            hits: [],
            nbHits: 0,
            nbPages: 0,
            processingTimeMS: 0,
          })),
        }).catch(err => {
          console.log(err);
        });
      }
      return algoliaClient.search(requests);
    },
  };

  const loaded = true;

  export default {
    data() {
      return {
        searchClient,
        nbHits: 0
      }
    },
    methods: {
      recipeToColor
    },
    components: {
      generateRecipeButton
    }

  };
</script>

<style>
  /* add bottom margin to search box */
  .ais-SearchBox {
    margin-bottom: 1em;
  }

  /* change search result from grid/box to row */
  .ais-Hits-list {
    padding-left: 0 !important;
  }

  .ais-Hits-item {
    border: none !important;
    padding: 0 !important;
    width: 100%;
    box-shadow: none;
    height: 3em;
    overflow: hidden;
  }

  .search-item {
    height: 100%;
    padding: 0.5em;
    text-decoration: none;
    color: black !important;
    font-weight: 600;
  }

  .search-item-ingredients {
    font-size: 0.75em !important
  }

  .ais-Pagination {
    padding-bottom: 50px !important;
    padding-top: 25px !important;
  }
</style>