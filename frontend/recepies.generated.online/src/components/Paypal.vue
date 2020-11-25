<template>
    <div id="smart-button-container">
        <div id="paypal-button-container"></div>
    </div>

</template>

<script>
    export default {
        props: ['recipeID', 'sendTo'],
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
                        return actions.order.create({
                            purchase_units: [{
                                "description": "Postkarte " +
                                    this.recipeID + ' an ' + this.sendTo.name + " " + this.sendTo.address + " " + this.senTo.ziz + " " + this.address.country,
                                "amount": {
                                    "currency_code": "EUR",
                                    "value": 4
                                }
                            }]
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