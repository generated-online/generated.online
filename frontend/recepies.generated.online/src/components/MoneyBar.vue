<template>
    <div
            style="width: 100%; margin-top: 1em; height: 100%; padding: 11px; vertical-align: center; text-shadow: none !important">
        <div
                style="width: 100%; height: 1.5em; border-radius: 5px; overflow: hidden; box-shadow: 0 0 10px black; background: rgba(1,1,1,0.8); color: white;">
            <div class="progress-item" :style="'width:' +  100* 2.20 / (price + money) + '%'">
                <b> 🖨 Druck
                </b>
            </div>
            <div class="progress-item" :style="'width:' +  100*0.70 / (price + money) + '%'">
                <b> 📪 Versand
                </b>
            </div>
            <div class="progress-item" :style="'width:' +  100* 0.35 / (price + money) + '%'">
                <b> 🏦 Paypal
                </b>
            </div>
            <div class="progress-item" :style="'width:' + 100* 0.25 / (price + money) + '%'">
                <b> 💻 Etc.
                </b>
            </div>
            <div v-show="money > 0" class="progress-item" style="border: none !important"
                 :style="'width:' + 100* money / (price + money) + '%'">
                <b> 🤩 Spenden
                </b>
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
<style scoped>
.progress-item {
    min-width: 1.4em;
    border-right: 1px solid white;
    padding-left: 0.5em;
    display: inline-flex;
}
</style>