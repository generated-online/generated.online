<template>
    <v-container>
        <DashboardNavBar/>
        <v-col v-if="user.loggedIn">
            <v-card class="boldyAppearing text-center heading my-5 text-h4 py-2 ma-auto" dark
                    style="width: fit-content">
                Orders
            </v-card>
            <v-row v-for="(order, idx) in filterOrders(orders, done=false)">
                <Order :key="idx" :order="order" class="mb-3"/>
            </v-row>
            <v-row class="pa-1 ma-2 black"></v-row>
            <v-row v-for="(order, idx) in filterOrders(orders, done=true)">
                <Order :key="idx" :order="order" class="mb-3"/>
            </v-row>
        </v-col>

        <v-alert v-else color="red"
                 dense
                 type="error"
                 class="ma-10">Please log in to view orders.</v-alert>
    </v-container>
</template>
<script>
import {mapGetters} from "vuex";
import DashboardNavBar from "@/components/dashboard/DashboardNavBar";
import firebase from "firebase";
import Order from "@/components/dashboard/Order";

export default {
    components: {Order, DashboardNavBar},
    computed: {
        // map `this.user` to `this.$store.getters.user`
        ...mapGetters({
            user: "user"
        })
    },
    data() {
        return {
            orders: []
        }
    },
    created() {
        this.getOrders()
    },
    mounted() {
        this.$emit('recipe', null);
    },
    methods: {
        getOrders() {
            let db = firebase.firestore();
            const ref = db.collection("orders")
            return ref.get().then(snap => {
                for (let doc of snap.docs) {
                    let data = doc.data()
                    data.id = doc.id
                    this.orders.push(data)
                }
            })
        },
        filterOrders(orders, done=false){
            return orders.filter(order => (order.done || false) === done)
        }
    }
};
</script>