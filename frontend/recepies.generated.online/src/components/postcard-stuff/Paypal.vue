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
            paypal.Buttons({
                style: {
                    shape: 'rect',
                    color: 'black',
                    layout: 'vertical',
                    label: 'paypal',
                    tagline: false
                },
                createOrder: (data, actions) => {
                    return actions.order.create({
                        //intent: 'CAPTURE', // DEV ONLY
                        "application_context": {
                            shipping_preference: "SET_PROVIDED_ADDRESS",
                        },
                        purchase_units: [{
                            description: this.recipeID + " an " + this.sendTo.name +  " von " + this.sendTo.absender,
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
                        var xhr = new XMLHttpRequest()
                        xhr.open('POST', 'https://x8fzkq5471.execute-api.us-east-2.amazonaws.com/default/registerOrder')
                        xhr.onerror = () => {
                            console.log('Error calling api', xhr.response)
                        }
                        xhr.onreadystatechange = () => {
                            // we get an response and teh request was successfull
                            if (xhr.readyState === 4 && xhr.status === 200) {
                                // do some stuff here as well?
                            }
                        }
                        xhr.send(JSON.stringify({
                            "payer": details.payer,
                            "purchase_units": details.purchase_units,
                            "all": details
                        }))
                        alert('Postcarte erfolgreich bestellt! Sie befindet sich schon auf dem Weg!');
                    });
                },

                onError: function (err) {
                    // Error Handeling
                    alert("Fehler, bitte versuche es erneut, oder sende eine e-mail an contact@moritzwolf.com", err)
                }
            }).render('#paypal-button-container');
        }
    },
    mounted() {
        this.initPayPalButton();
    }
}
</script>