<template>
    <v-container>
        <DashboardNavBar/>
        <v-card dark class="boldyAppearing text-center heading my-5 text-h4 py-2 ma-auto" style="width: fit-content">
            Orders
        </v-card>
        <Order v-for="(order, idx) in orders" :order="order" :key="idx" class="mb-3"/>

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
        if (this.user && this.user.loggedIn) {
            this.getOrders()
        }

    },
    methods: {
        getOrders() {
            let db = firebase.firestore();
            const ref = db.collection("orders")
            return ref.get().then(snap => {
                for (let doc of snap.docs) {
                    this.orders.push(doc.data())
                }
            })
        }
    }
};
</script>