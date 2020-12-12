<template>
    <div class="wrapper">
        <div class="progress-padding" :style="flexStyle(2.21, minWidth)+'; '+bg(color='yellow')">
            🖨 2.20€
        </div>
        <div class="progress-padding progress-border-left" :style="flexStyle(0.7, minWidth)+'; '+bg(color='skyblue')">
            📪 0.7€
        </div>
        <div class="progress-padding progress-border-left"
             :style="flexStyle(0.35, minWidth)+'; '+bg(color='lightseagreen')">
            🏦 0.35€
        </div>
        <div class="progress-padding progress-border-left"
             :style="flexStyle(0.25, minWidth)+'; '+bg(color='lightpink')">
            💻 0.25€
        </div>
        <transition name="section">
            <div v-show="money > 0" class="progress-padding progress-border-left spendenBackground"
                 :style="flexStyle(money, minWidth)">
                <div class="rotation" style="float: left; margin-left: 25%">🤩</div>
                <div style="float: left"> Spenden</div>
            </div>
        </transition>
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
        bg(color) {
            return "background-color: " + color + ";box-shadow: 0 0 10px " + color
        }
    }
}
</script>

<style scoped>
.wrapper {
    width: 100%;
    height: 1.5em;
    overflow: hidden;
    display: flex;
    border-radius: 5px;
    color: black;
}

.progress-padding {
    text-align: center;
    padding-left: 0.1em;
}

.spendenBackground {
    background: linear-gradient(-90deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: slide 5s ease-in infinite;
}

@keyframes slide {
    0% {
        background-position: 0 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0 50%;
    }
}

.rotation {
    animation: rotate 2s linear infinite;
}

@keyframes rotate {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}

</style>