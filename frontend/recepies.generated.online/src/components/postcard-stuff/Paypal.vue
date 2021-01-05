<template>
    <div id="smart-button-container" style="position: relative; z-index: 1;">
        <div id="paypal-button-container"></div>
    </div>
</template>

<script>
    export default {
        props: ['recipeID', 'sendTo', 'amount'],
        methods: {
            initPayPalButton() {
                let _this = this
                paypal.Buttons({
                    style: {
                        shape: 'rect',
                        color: 'black',
                        layout: 'vertical',
                        label: 'paypal',
                        tagline: false
                    },
                    createOrder: (data, actions) => {
                        this.$analytics.logEvent("paypal_created_order");
                        return actions.order.create({
                            //intent: 'CAPTURE', // DEV ONLY
                            "application_context": {
                                shipping_preference: "SET_PROVIDED_ADDRESS",
                            },
                            purchase_units: [{
                                description: this.recipeID + " an " + this.sendTo.name +
                                    " von " + this.sendTo.absender,
                                amount: {
                                    currency_code: "EUR",
                                    value: this.amount
                                },
                                shipping: {
                                    name: {
                                        full_name: this.sendTo.name
                                    },
                                    address: {
                                        address_line_1: this.sendTo.street,
                                        postal_code: this.sendTo.plz,
                                        admin_area_2: this.sendTo.city,
                                        country_code: this.sendTo.country
                                    }
                                }
                            }],
                        });
                    },
                    onApprove: function (data, actions) {
                        _this.$analytics.logEvent("paypal_order_worked");
                        return actions.order.capture().then(function (details) {

                            let db = firebase.firestore();
                            db.collection("orders").doc().set({
                               "sendTo": _this.sendTo,
                                "all": details
                            })
                            _this.$analytics.logEvent("paypal_order_registered");

                            alert('Postcarte erfolgreich bestellt! Sie befindet sich schon auf dem Weg!');
                        });
                    },

                    onError: function (err) {
                        // Error Handeling
                        alert("Fehler, bitte versuche es erneut, oder sende eine e-mail an contact@moritzwolf.com",
                            err)
                        _this.$analytics.logEvent("paypal_error_happened");
                    }
                }).render('#paypal-button-container');
            }
        },
        mounted() {
            this.initPayPalButton();
        }
    }
</script>