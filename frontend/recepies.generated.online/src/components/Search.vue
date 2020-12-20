<template>
    <div>
        <ais-instant-search :routing="routing" :search-client="searchClient" index-name="Recipes">

            <ais-search-box attribute="title" placeholder="Suche nach Rezepten..." reset-title="Lösche alles"
                            show-loading-indicator submit-title="Suche"/>

            <ais-refinement-list :limit="0" :searchable="false" :show-more="true"
                                 :sort-by="['count:desc']"
                                 attribute="filtered_ingredients"
                                 operator="and" searchable-placeholder="Suche nach Zutaten...">

                <v-col slot-scope="{
                                      items,
                                      isShowingMore,
                                      canToggleShowMore,
                                      refine,
                                      createURL,
                                      toggleShowMore,
                                      canRefine
                                    }"
                >
                    <!--                    here we have one centered flex row filled with refinements/ingredients -->
                    <v-row cols="auto" justify="center">
                        <v-col v-for="item in items"
                               :class="[ 'ma-1' ,'py-1', 'px-2',{'boldy':!item.isRefined, 'boldy-red':item.isRefined}]"
                               :href="createURL(item.value)"
                               align="center"
                               cols="auto"
                               @click.prevent="refine(item.value)"
                        >
                            {{ item.count.toLocaleString() }} x <img :src="wordToEmoji(item.label)" class="emoji"/>
                            <ais-highlight v-if="!wordToEmoji(item.label)" :hit="item" attribute="item"/>
                        </v-col>
                    </v-row>
                    <!-- this row contains just buttons for showing/hiding/clearing refinements-->
                    <v-row class="mt-3" justify="center">
                        <ais-clear-refinements>
                            <div slot-scope="{ canRefine, refine, createURL }">
                                <v-btn v-if="canRefine"
                                       :href="createURL()"
                                       class="black-button"
                                       @click.prevent="refine"
                                >
                                    Zutaten löschen
                                </v-btn>
                                <!-- this is only used here because outside this tag i can not use the canRefine variable-->
                                <v-btn v-if="canToggleShowMore && isShowingMore && !canRefine"
                                       class="black-button"
                                       @click.prevent="toggleShowMore"
                                >
                                    Erweiterte Suche Schließen
                                </v-btn>
                            </div>
                        </ais-clear-refinements>
                        <!-- for some reason canRefine works differently in the ais-clear-refinement tag
                             can not use it to hide this button when a refinement is active-->
                        <v-btn
                                v-if="canToggleShowMore && !isShowingMore"
                                class="black-button"
                                @click="toggleShowMore"
                        >
                            {{ !isShowingMore ? 'Erweiterte Suche' : 'Erweiterte Suche Schließen' }}
                        </v-btn>
                    </v-row>
                </v-col>
            </ais-refinement-list>


            <ais-state-results>
                <template slot-scope="{ state: { query }, results: { hits, nbPages } }">
                    <ais-hits>
                        <v-row slot="item" slot-scope="{ item }"
                               :style="{'color':(recipeToColor(item.objectID) +' !important')}">
                            <RecipeCard
                                    :recipe="{'id': item.objectID, 'votes':0, 'title':item.title, 'ingredients':item.ingredients}"/>
                        </v-row>
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

import RecipeCard from "@/components/RecipeCard";
import recipeToColor from "@/functions/recipe_to_color";
import generateRecipeButton from "@/components/generateRecipeButton";
import {wordToEmoji} from "@/functions/emojiUtils";

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
        recipeToColor,
        wordToEmoji
    },
    components: {
        generateRecipeButton,
        RecipeCard
    },
    mounted() {
        // this makes sure that the provided search history uses replace state instead of push state
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
  //margin-bottom: 0.5em;
}

/* change search result from grid/box to row */
.ais-Hits-list {
  padding-left: 0 !important;
}

.ais-Hits-item {
  border: none !important;
  padding: 0 !important;
  margin-left: 1em;
  margin-right: 1em;
  margin-top: 0;
  width: 100%;
  box-shadow: none;
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

.ais-SearchBox-submitIcon {
  width: 1.5em !important;
  height: 1.5em !important;
  margin-left: 1em !important;
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

.emoji {
  vertical-align: middle;
  height: 1em;
}
</style>