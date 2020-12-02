<template>
    <div style="width: 100%; margin-top: 1em; height: 100%; vertical-align: center; text-shadow: none !important">
        <div style="width: 100%; height: 1.5em; overflow: hidden;" class="shady">
            <div class="progress-item" :style="'width:' +  100* 2.20 / (price + money) + '%'">
                🖨 Druck
            </div>
            <div class="progress-item" :style="'width:' +  100*0.70 / (price + money) + '%'">
                📪 Versand
            </div>
            <div class="progress-item" :style="'width:' +  100* 0.35 / (price + money) + '%'">
                🏦 Paypal
            </div>
            <div class="progress-item" :style="'width:' + 100* 0.25 / (price + money) + '%'">
                💻 Etc.

            </div>
            <div v-show="money > 0" class="progress-item" style="border: none !important"
                :style="'width:' + 100* money / (price + money) + '%'">
                🤩 Spenden

            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'MoneyBar',
        props: {
            money: {},
            price: {}
        }
    }
</script>
<style>
    .shady {
        border-radius: 5px;
        box-shadow: 0 0 10px black;
        background: rgba(1, 1, 1, 0.8);
        color: white;
    }

    .progress-item {
        min-width: 1.4em;
        border-right: 1px solid white;
        padding-left: 0.5em;
        display: inline-flex;
    }
</style>