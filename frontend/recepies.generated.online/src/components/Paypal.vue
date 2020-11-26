<template>
    <div id="smart-button-container">
        <div id="paypal-button-container"></div>
    </div>

</template>

<script>
    export default {
        props: ['recipeID', 'sendTo', 'amount'],
        methods: {
            initPayPalButton() {
                paypal.Buttons({
                    style: {
                        shape: 'rect',
                        color: 'black',
                        layout: 'vertical',
                        label: 'paypal',

                    },

                    createOrder: (data, actions) => {
                        console.log(this.recipeID);
                        console.log(this.sendTo);
                        return actions.order.create({
                            //intent: 'CAPTURE', // DEV ONLY
                            "application_context": {
                                shipping_preference: "SET_PROVIDED_ADDRESS",
                            },
                            purchase_units: [{
                                description: "Postkarte " +
                                    window.location.href + " an " + this.sendTo.name + " " + this
                                    .sendTo.street + " " + this.sendTo.zip + " " + this
                                    .sendTo.country,
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
                        return actions.order.capture().then(function (details) {
                            alert('Transaction completed by ' + details.payer.name.given_name +
                                '!');
                        });
                    },

                    onError: function (err) {
                        console.log(err);
                    }
                }).render('#paypal-button-container');
            }
        },
        mounted() {
            this.initPayPalButton();
            // this makes sure we catch the event in the background rendering
            window.dispatchEvent(new Event('resize'))
        }
    }
</script>