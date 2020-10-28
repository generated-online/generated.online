<template>
  <div>
      <ais-instant-search
        :search-client="searchClient"
        index-name="Recipes"
      >

        <ais-search-box />

        <ais-hits>
          <div slot="item" slot-scope="{ item }">
            <router-link :to="'/recipe/' + item.objectID"><ais-highlight attribute="title" :hit="item"/></router-link>
          </div>
        </ais-hits>

        <ais-state-results>
          <template slot-scope="{ state: { query }, results: { hits, nbPages } }">
            <!-- show no result if query with no hits -->
            <div v-if="query && hits.length == 0">Keine Treffer!</div>

            <!-- hide pagination if 1 or less pages -->
            <ais-pagination v-if="nbPages > 1"/>
          </template>
        </ais-state-results>

      </ais-instant-search>
  </div>
</template>

<script>
import algoliasearch from 'algoliasearch/lite'
import 'instantsearch.css/themes/algolia-min.css'


const algoliaClient = algoliasearch(
  '7KL69V3MEL', // Application ID
  '6facf15b54148bc84e399e2994885c15'  // Search-Only API Key
)

// this setup is required to prevent search on empty query
const searchClient = {
  search(requests) {
    if (requests.every(({ params }) => !params.query)) {
     return Promise.resolve({
        results: requests.map(() => ({
          hits: [],
          nbHits: 0,
          nbPages: 0,
          processingTimeMS: 0,
        })),
      }).catch( err => {console.log(err);});
    }
    return algoliaClient.search(requests);
  },
};


export default {
  data() {
    return {
      searchClient
    }
  },
};
</script>

<style scoped>
/* add bottom margin to search box */
.ais-SearchBox {
  margin-bottom: 1em;
}

/* change search result from grid/box to row */
.ais-Hits-item {
  width: 100%;
  border: none;
  box-shadow: none;

}

/* prevent highlight overwrite font-size */
.ais-Highlight {
  font-size: inherit;
}
.ais-Highlight-highlighted {
  font-size: inherit;
}
</style>