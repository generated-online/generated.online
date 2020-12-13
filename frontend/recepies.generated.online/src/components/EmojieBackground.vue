<template>
    <div :style="backgroundMargin" >
        <div v-for='_row in numRow' :key="_row">
            <!-- uneven rows vue starts indexing at 1 lol-->
            <div :style="row">
                <div v-if="_row % 2 === 0" :style="uneven">
                    <div v-for='element in elementsInRow+2' :key="element" :style="emojiContainer"
                        class="emojie-container">
                        <div class="emojie">
                            <img :class="[{'emojie-animation': showEmojies}, {'hide': !showEmojies}]" :src="getImgUrl(line[element - 1])"
                                :style="emoji">
                        </div>
                    </div>
                </div>
                <!-- even rows -->
                <div v-else :style="even">
                    <div v-for='element in (elementsInRow+1)' :key="element" :style="emojiContainer"
                        class="emojie-container">
                        <div class="emoji">
                            <img :class="[{'emojie-animation': showEmojies}, {'hide': !showEmojies}]" :src="getImgUrl(reverseLine[element - 1])"
                                :style="emoji">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {
        getEmojiLines,
        getImgUrl
    } from "@/functions/emojiUtils";

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
                showEmojies: false,
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
            storeEmojiLines() {
                var lines = getEmojiLines(this.recipe, this.elementsInRow)
                this.line = lines[0]
                this.reverseLine = lines[1]

                // trigger animation
                this.showEmojies = false
                setTimeout(() => {
                    this.showEmojies = true
                }, 10)
            },
            getImgUrl
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
.hide {
    display: none;
}
    .emojie-container {
        float: left;
        text-align: center;
        display: table;
    }

    @keyframes fade-in {
        from {
            opacity: 0;
        }

        to {
            opacity: 1;
        }
    }

    .emojie-animation {
        animation: fade-in 1s forwards;
        -webkit-animation: fade-in 1s forwards;
        opacity: 0;
    }

    .emoji {

        display: table-cell;
        vertical-align: middle;
    }
</style>