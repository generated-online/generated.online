<template>
    <div>
        <ais-instant-search :routing="routing" :search-client="searchClient" index-name="Recipes">

            <ais-search-box attribute="title" placeholder="Suche nach Rezepten..." reset-title="Lösche alles"
                            show-loading-indicator submit-title="Suche"/>

            <ais-refinement-list :limit="0" :searchable="false" :show-more="true"
                                 :sort-by="['count:desc']"
                                 :transform-items="transformIngredient"
                                 attribute="filtered_ingredients" operator="and"
                                 searchable-placeholder="Suche nach Zutaten...">

                <v-col v-if="canToggleShowMore" slot-scope="{
                                      items,
                                      isShowingMore,
                                      canToggleShowMore,
                                      refine,
                                      createURL,
                                      toggleShowMore,
                                      canRefine
                                    }"
                >
                    <!--here we have one centered flex row filled with refinements/ingredients -->
                    <v-row cols="auto" justify="center">
                        <v-col v-for="item in items"
                               :class="[ 'ma-1' ,'py-1', 'px-2',{'boldy':!item.isRefined, 'boldy-red':item.isRefined}]"
                               :href="createURL(item.value)"
                               cols="auto"
                               @click.prevent="refine(item.value)"
                        >
                            {{ item.count.toLocaleString() }} x <img v-if="item.emoji" :alt="item.label"
                                                                     :src="item.emoji"
                                                                     class="emoji"/>
                            <ais-highlight v-if="!item.emoji" :hit="item" attribute="item"/>
                        </v-col>
                    </v-row>
                    <!-- this row contains just buttons for showing/hiding/clearing refinements-->
                    <v-row justify="center">
                        <ais-clear-refinements>
                            <div slot-scope="{ canRefine, refine, createURL }">
                                <v-btn v-if="canRefine"
                                       :href="createURL()"
                                       class="boldyNoColor ma-2"
                                       dark
                                       style="color: rgb(231, 55, 61)"
                                       @click.prevent="refine"
                                >
                                    <v-icon class="mx-1">delete</v-icon>
                                    <v-icon class="mx-1">filter_alt</v-icon>
                                </v-btn>
                                <!-- this is only used here because outside this tag i can not use the canRefine variable-->
                                <v-btn v-if="canToggleShowMore && isShowingMore && !canRefine"
                                       class="boldy ma-2"
                                       dark
                                       @click.prevent="toggleShowMore"
                                >
                                    <v-icon class="mx-1">close_fullscreen</v-icon>
                                    <v-icon class="mx-1">filter_alt</v-icon>
                                </v-btn>
                            </div>
                        </ais-clear-refinements>
                        <!-- for some reason canRefine works differently in the ais-clear-refinement tag
                             can not use it to hide this button when a refinement is active-->
                        <v-btn
                                v-if="canToggleShowMore && !isShowingMore"
                                class="boldy ma-2"
                                dark
                                @click="toggleShowMore"
                        >
                            <v-icon class="mx-1">filter_alt</v-icon>
                        </v-btn>
                    </v-row>
                </v-col>
                <div v-else>

                </div>
            </ais-refinement-list>

            <ais-state-results>
                <template slot-scope="{ state: { query }, results: { hits, page, nbPages } }">

                    <ais-infinite-hits v-if="query && hits.length !== 0" :cache="cache">
                        <v-col slot-scope="{ items, filteredItems,refineNext,isLastPage }">
                            <v-row v-for="item in items"
                                   :style="{'color':(recipeToColor(item.objectID) +' !important')}">
                                <RecipeCard :key="item.objectID"
                                        :recipe="{'id': item.objectID, 'votes':'', 'title':item.title, 'ingredients':item.ingredients}"/>
                            </v-row>
                            <!--automatically load next page-->
                            <!--somehow this does not work in mobile -> dont show-->

                            <v-row :style="'opacity: '+ (isLastPage?0:1)"
                                   align="center" class="loadingBox shady"
                                   no-gutters>
                                <v-progress-circular color="black" indeterminate size="40"></v-progress-circular>
                                <div v-if="!isLastPage && scrolledToBottom">{{
                                        loadNextResults(refineNext, scrollPos())
                                    }}
                                </div>
                            </v-row>
                        </v-col>

                    </ais-infinite-hits>

                    <!-- show no result if query with no hits -->
                    <v-row v-if="query && hits.length === 0" justify="center">
                        <v-btn class="boldy-red px-4 py-1 my-6" large>
                            <h2 class="text-capitalize" style="width: fit-content">Keine Treffer</h2>
                            <v-icon style="padding-left:0.5em">error</v-icon>
                        </v-btn>
                    </v-row>

                    <!-- random recipe button-->
                    <v-row v-if="hits.length === 0" justify="center">
                        <generateRecipeButton/>
                    </v-row>
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
import {createInfiniteHitsSessionStorageCache} from 'instantsearch.js/es/lib/infiniteHitsCache'

import RecipeCard from "@/components/RecipeCard";
import recipeToColor from "@/functions/recipe_to_color";
import generateRecipeButton from "@/components/generateRecipeButton";
import {wordToEmoji} from "@/functions/emojiUtils";

// const algoliaClient = algoliasearch(
//    '7KL69V3MEL', // Application ID
//    '6facf15b54148bc84e399e2994885c15' // Search-Only API Key
//)
//const algoliaClient = algoliasearch(
//    'D6W68MPLE5', // Application ID
//    '84f604b3c2c1684ed632a6a9e46e1502' // Search-Only API Key
//)

const algoliaClient = algoliasearch(
    'IFRMJQG34A', // Application ID
    '4273c69871b444a3e008225d42016938' // Search-Only API Key
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
            cache: createInfiniteHitsSessionStorageCache(),
            scrolledToBottom: false,
            lastScrollPosition: -1,
        }
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

        // listen for scrolled to bottom
        let whitelist = ['setScroll'];
        this.$store.subscribe((mutation, state) => {
            if (whitelist.includes(mutation.type)) {
                this.scrolledToBottom = state.scrolledToBottom
            }
        });
    },
    methods: {
        recipeToColor,
        wordToEmoji,
        transformIngredient(ingredients) {
            ingredients.map((ingredient) => {
                ingredient.emoji = wordToEmoji(ingredient.label)
            })
            return ingredients
        },
        loadNextResults(refineNext, currScrollPosition) {
            if (Math.abs(this.lastScrollPosition - currScrollPosition) < 20) return
            this.lastScrollPosition = currScrollPosition
            refineNext()
        },
        scrollPos(){
            return window.pageYOffset ||  0
        }
    }
};
</script>

<style lang="scss">

// SEARCH

/* change search result from grid/box to row */
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

.ais-SearchBox-submitIcon {
  width: 1.5em !important;
  height: 1.5em !important;
  margin-left: 1em !important;
}

input:focus {
  outline: none;
}

input::placeholder {
  color: white !important;
}

// sarch icon is made white here
path {
  fill: white !important;
}

// and this is for the results
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

.emoji {
  vertical-align: middle;
  height: 1em;
}

.loadingBox {
  margin: auto;
  padding: 2px;
  width: fit-content;
  border-radius: 50px;
  box-shadow: 0 0 10px rgba(128, 128, 128, 0.8);
  background: rgba(228, 228, 228, 0.9);
  color: black;
}
</style>