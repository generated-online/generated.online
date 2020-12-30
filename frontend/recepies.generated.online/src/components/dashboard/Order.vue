<template>
    <v-card class="boldyAppearing" dark style="width: 100%">
        <v-card-title>
            <span class="headline">{{ order.all.payer.name.surname }} {{ order.all.payer.name.given_name }}</span>
        </v-card-title>
        <v-spacer></v-spacer>
        <v-card-text v-if="recipes.length" v-for="(purchase, idx) in order.all.purchase_units" :key="idx">
            <v-row >
                <v-col cols="auto">
                    {{ purchase.shipping.name.full_name }}
                    <br>
                    {{ purchase.shipping.address.address_line_1 }}
                    <br>
                    {{ purchase.shipping.address.postal_code }} {{ purchase.shipping.address.admin_area_2 }}
                    <br>
                    {{ purchase.shipping.address.country_code }}
                </v-col>
                <v-col cols="auto">
                    {{ purchase.amount.value }} {{ purchase.amount.currency_code }}
                </v-col>
                <v-col cols="auto">
                    id: {{ purchase.description.split(" ")[0] }}
                    <br>
                    an: {{ purchase.description.split("von").slice(-1)[0] }}
                    <br>
                    <v-btn icon @click="showDialog = true">
                        <v-icon>download</v-icon>
                    </v-btn>
                    <DownloadPopup v-if="showDialog" :query="{
                    'absender': purchase.description.split('von').slice(-1)[0],
                    'country': purchase.shipping.address.country_code,
                    'name': purchase.shipping.name.full_name,
                    'recipe': recipes[idx],
                    'street': purchase.shipping.address.address_line_1,
                    'zip': purchase.shipping.address.postal_code + ' ' + purchase.shipping.address.admin_area_2
                    }" :show-dialog.sync="showDialog"
                    ></DownloadPopup>
                    <v-row no-gutters style="width: 10px; height: 200px; font-size: 1em">
                        <Postcard v-if="recipes[idx]"
                                  :horizontal="false"
                                  :parent-width="150" :recipe='recipes[idx]'
                        />
                    </v-row>

                </v-col>
                <v-col>
                    {{ purchase.payee.email_address }}
                </v-col>
            </v-row>
        </v-card-text>
    </v-card>
</template>

<script>
import DownloadPopup from "@/components/DownloadPopup";
import {loadRecipe} from "@/functions/recipeUtils";
import Postcard from "@/components/postcard-stuff/Postcard";

export default {
    name: "Order",
    components: {
        DownloadPopup,
        Postcard
    },
    props: ["order"],
    data() {
        return {
            showDialog: false,
            recipes: [],
            loaded_all_recipes: false
        }
    },
    mounted() {
        this.order.all.purchase_units.forEach((purchase, idx) => {
            loadRecipe(purchase.description.split(" ")[0]).then((recipe) => {
                this.recipes.push(recipe)
            });
        })
    }
}
</script>

<style scoped>
</style>