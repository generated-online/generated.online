<template>
    <div id="smart-button-container">
        <div style="text-align: center;">
            <div id="paypal-button-container"></div>
        </div>
    </div>

</template>

<script>
    export default {
        props: ['recipe', 'color'],
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
                                "description": "Versende eine Postkarte mit einem Rezept! ID: " +
                                    this.recipe.id,
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
        }
    }
</script>

<style scoped>
#smart-button-container {
    padding: 10em;
}
</style>