<template>
    <div>
        <ais-instant-search :routing="routing" :search-client="searchClient" index-name="Recipes">

            <ais-search-box attribute="title" placeholder="Suche nach Rezepten..." reset-title="Lösche alles"
                            show-loading-indicator submit-title="Suche"/>

            <ais-refinement-list :class-names="{
          'ais-RefinementList-showMore': 'showMore-button',
          'ais-RefinementList-showMore--disabled': 'showMore-button--disbaled',
          }" :limit="5" :searchable="false" :show-more="true"
                                 :sort-by="['count:desc']"
                                 attribute="filtered_ingredients" class="bg-color"
                                 operator="and" searchable-placeholder="Suche nach Zutaten..."/>

            <ais-state-results class="text-center">
                <template slot-scope="{ state: { query }, results: { hits, nbPages } }">
                    <ais-hits class="ais-hits">
                        <div slot="item" slot-scope="{ item }" :style="'background-color:'+recipeToColor(item.objectID)"
                             class="search-item" @click="$router.push('/recipe/' + item.objectID)">
                            <ais-highlight :hit="item" attribute="title"/>
                            <div>
                <span v-for="ingredient in item.ingredients" :key="ingredient+String(Math.floor(Math.random() * 10000))"
                      class="search-item-ingredients">{{ ingredient }}</span>
                            </div>
                        </div>
                    </ais-hits>
                    <!-- show no result if query with no hits -->
                    <v-btn v-if="query && hits.length == 0" class="boldy-red ma-auto px-4 py-1" large>
                        <h2 class="text-capitalize" style="width: fit-content">Keine Treffer {{ query }}</h2>
                        <v-icon style="padding-left:0.5em">error</v-icon>
                    </v-btn>
                    <!-- hide pagination if 1 or less pages -->
                    <ais-pagination v-if="nbPages > 1"/>
                    <div v-if="hits.length == 0" style="text-align:center">
                        <generateRecipeButton/>
                    </div>
                </template>
            </ais-state-results>

        </ais-instant-search>
    </div>
</template>

<script>
import {history} from 'instantsearch.js/es/lib/routers';
import {simple} from 'instantsearch.js/es/lib/stateMappings';
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
    searchForFacetValues: function (requests) {
        return algoliaClient.searchForFacetValues(requests);
    },
}


export default {
    data() {
        return {
            searchClient,
            nbHits: 0,
            routing: {
                router: history(),
                stateMapping: simple(),
            },
        }
    },
    methods: {
        recipeToColor
    },
    components: {
        generateRecipeButton
    },
    mounted() {
        this.routing.router.write = function (routeState) {
            var _this = this;

            var url = this.createURL(routeState);
            if (this.writeTimer) {
                window.clearTimeout(this.writeTimer);
            }

            this.writeTimer = window.setTimeout(function () {
                window.history.replaceState(routeState, '', url);
                _this.writeTimer = undefined;
            }, this.writeDelay);
        }
    }
};
</script>

<style lang="scss">
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

.ais-RefinementList {
  padding-bottom: 25px !important;
}

.ais-Pagination {
  padding-bottom: 50px !important;
  padding-top: 25px !important;
}

.showMore-button,
.showMore-button:focus {
  background-color: transparent;
  color: black;
  border: thin solid black;
}

.ais-SearchBox-submitIcon {
  width: 1.5em !important;
  height: 1.5em !important;
  margin-left: 1em !important;
}

.showMore-button:hover {
  background-color: lightgray;
}

.showMore-button--disbaled,
.showMore-button--disabled:hover {
  display: none;
}

.ais-SearchBox-input {
  padding-left: 50px !important;
  font-size: 2em;
  background: rgba(1, 1, 1, 1);
  border-radius: 15px;
  border: 1px solid rgba(1, 1, 1, 0.8);
  color: var(--bg-color) !important;
  user-select: inherit !important;
}

@media (max-width: 600px) {
  .ais-SearchBox-input {
    font-size: 1em !important;
  }
}

input:focus {
  outline: none;
}

input::placeholder {
  color: white !important;
}

path {
  fill: white !important;
}
</style>