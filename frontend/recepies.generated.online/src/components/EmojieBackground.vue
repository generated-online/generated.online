<template>
    <div class="background" :style="backgroundMargin+' background: '+color">
        <div v-for='_row in numRow' :key="_row">
            <!-- uneven rows vue starts indexing at 1 lol-->
            <div :style="row">
                <div v-if="_row % 2 === 0" :style="uneven">
                    <div class="emojie-container" :style="emojiContainer" v-for='element in elementsInRow+2'
                        :key="element">
                        <div class="emoji">
                            <img :style="emoji" :src="getImgUrl(line[element - 1])">
                        </div>
                    </div>
                </div>
                <!-- even rows -->
                <div v-else :style="even">
                    <div class="emojie-container" :style="emojiContainer" v-for='element in (elementsInRow+1)'
                        :key="element">
                        <div class="emoji">
                            <img :style="emoji" :src="getImgUrl(reverseLine[element - 1])">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {getEmojiLines} from "@/functions/emojiUtils";

export default {
        props: {
            "recipe": {
                type: Object,
                default: () => {}
            },
            "emojiContainerSize": {
                type: String,
                default: "5em"
            },
            "emojieSize": {
                type: String,
                default: "3em"
            },
            "opacity": {
                type: Number,
                default: 0.2
            },
            "color": {
                type: String,
                default: "lightblue"
            }
        },
        data() {
            return {
                width: window.innerWidth,
                height: window.innerHeight,
                elementsInRow: 1,
                numRow: 1,
                rowMargin: "5px",
                line: [],
                reverseLine: [],
                matchingEmos: [],
                emoMapKeys: {},
                allPossibleEmos: [],
            }
        },
        methods: {
            getImgUrl(emojie) {
                if (emojie === undefined) emojie = "knoblauch"

                var images = require.context('@/assets/emojies/', false, /\.png$/)
                return images('./' + emojie + ".png")
            },
            calculateElementsInRow() {
                var width = this.$el.offsetWidth;
                var elementWidthInPx = this.emToPixle(this.emojiContainerSize);
                this.elementsInRow = Math.floor(width / elementWidthInPx) - 1;
                this.rowMargin = (width - (this.elementsInRow + 1) * elementWidthInPx) / 2 + "px"
            },
            calculateNumRows() {
                var height = this.$el.offsetHeight;
                var rowHeight = this.emToPixle(this.emojiContainerSize);
                this.numRow = Math.floor(height / rowHeight) + 1; // +1 because of negative margin top and bottom
            },
            dictToCssString(d) {
                // this generates correct css string out of object
                var s = ""
                for (var key in d) {
                    s += key + ": " + d[key] + "; "
                }
                return s
            },
            emToPixle(emValue) {
                var em = parseFloat(getComputedStyle(this.$parent.$el).fontSize);
                return parseFloat(emValue) * em
            },
            storeEmojiLines(){
                var lines = getEmojiLines(this.recipe, this.elementsInRow)
                this.line = lines[0]
                this.reverseLine = lines[1]
            }
        },
        created() {
        },
        mounted() {
            this.calculateElementsInRow()
            this.calculateNumRows()
            this.storeEmojiLines()

            let ob = new ResizeObserver((mutationList, a) => {
                this.height = mutationList[0].target.clientHeight
                this.width = mutationList[0].target.clientWidth
            })
            ob.observe(this.$parent.$el)
        },
        watch: {
            "recipe": function () {
                this.storeEmojiLines()
            },
            "height": function () {
                this.calculateNumRows()
            },

            "width": function () {
                this.calculateElementsInRow()
                this.storeEmojiLines()
            }
        },
        computed: {
            emojiContainer() {
                var d = {
                    "height": this.emojiContainerSize,
                    "width": this.emojiContainerSize,
                    "opacity": this.opacity
                }
                return this.dictToCssString(d)
            },
            emoji() {
                var d = {
                    "height": this.emojieSize,
                    "width": this.emojieSize,
                }
                return this.dictToCssString(d)
            },
            row() {
                return this.dictToCssString({
                    "margin-left": this.rowMargin,
                    "margin-right": this.rowMargin
                })
            },
            even() {
                return ""
            },
            uneven() {
                return this.dictToCssString({
                    "margin-left": "-" + this.emToPixle(this.emojiContainerSize) / 2 + "px",
                    "margin-right": "-" + this.emToPixle(this.emojiContainerSize) / 2 + "px",
                    // "margin-right": -this.rowMargin
                })
            },
            halfSpacer() {
                return "float: left; width:" + parseFloat(this.emojiContainerSize) / 2 +
                    "em; background: transparent; height: " + this.emojiContainerSize
            },
            backgroundMargin() {
                return this.dictToCssString({
                    "margin-top": "-" + parseFloat(this.emojiContainerSize) / 2 + "em",
                })
            }

        }
    }
</script>

<style scoped>
    .background {
        pointer-events: none;
        position: absolute;
        top: 0em;
        right: 0;
        left: 0;
        overflow: hidden;
        bottom: 0px;
        -webkit-touch-callout: none;
        -webkit-user-select: none;
        -khtml-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        z-index: -1;
    }

    .emojie-container {
        float: left;
        text-align: center;
        display: table;
    }

    .emoji {
        display: table-cell;
        vertical-align: middle;
    }
</style>