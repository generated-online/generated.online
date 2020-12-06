<template>
    <div style="width: 100%; margin-top: 1em; height: 100%; vertical-align: center; text-shadow: none !important">
        <div style="width: 100%; height: 1.5em; overflow: hidden; display: flex;" class="light-shady">
            <div class="progress-padding" :style="flexStyle(2.21, minWidth)+'; '+bg(color='yellow')">
                🖨 Druck
            </div>
            <div class="progress-padding progress-border-left" :style="flexStyle(0.7, minWidth)+'; '+bg(color='skyblue')">
                📪
            </div>
            <div class="progress-padding progress-border-left"
                 :style="flexStyle(0.35, minWidth)+'; '+bg(color='lightseagreen')">
                🏦
            </div>
            <div class="progress-padding progress-border-left" :style="flexStyle(0.25, minWidth)+'; '+bg(color='lightpink')">
                💻
            </div>
            <transition name="section">
                <div v-show="money > 0" class="progress-padding progress-border-left spendenBackground"
                     :style="flexStyle(money, minWidth)">
                    🤩 Spenden
                </div>
            </transition>
        </div>
    </div>
</template>
<script>
export default {
    name: 'MoneyBar',
    props: {
        money: {},
        price: {}
    },
    data() {
        return {"minWidth": "2em"}
    },
    methods: {
        flexStyle(proportion, minWidth) {
            return 'flex: ' + proportion + ";min-width: " + minWidth
        },
        bg(color){
            return "background-color: " + color + ";box-shadow: 0 0 10px " + color
        }
    }
}
</script>

<style scoped>
.light-shady {
    border-radius: 5px;
    box-shadow: 0 0 10px black;
    background: rgba(1, 1, 1, 0.8);
    color: black;
    text-align: center;
}

.progress-padding {
    text-align: center;
    padding-left: 0.1em;
}

.progress-border-left {
    border-left: 1px solid white;
    border-right: 1px solid transparent;
}

.spendenBackground {
    background: linear-gradient(-90deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: slide 5s ease infinite;
}

@keyframes slide {
    0%{background-position:0 50%}
    50%{background-position:100% 50%}
    100%{background-position:0 50%}
}

</style>