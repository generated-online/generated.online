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
                emoMap: {
                    'rind': 'steak',
                    'speck': 'schinken',
                    'haselnüsse': 'kastanie',
                    "lachs": 'fisch',
                    "forelle": 'fisch',
                    "brasse": 'fisch',
                    "karpfen": 'fisch',
                    "hecht": 'fisch',
                    "äpfel": 'apfel',
                    "möhre": "karotte",
                    "gelberübe": "karotte",
                    "eigelb": "ei",
                    "thymian": "kräuter",
                    "oregano": "kräuter",
                    "basilikum": "samen",
                    "petersilie": "kräuter",
                    "fleisch": "steak",
                    "parmesan": "käse",
                    "gorgonzola": "käse",
                    "gauda": "käse",
                    "emmenthaler": "käse",
                    "erdnüsse": "erdnuss",
                    "haselnüsse": "haselnuss",
                    "manderine": "orange",
                    "clementine": "orange",
                    "schwammerl": "pilze",
                    "champignons": "pilze",
                    "eigelb": "ei",
                    "eiweiß": "ei",
                    "filet": "steak",
                    "braten": "steak",
                    "hühnchen": "juhn",
                    "pute": "truthahn",
                    "geflügel": "ente",
                    "plätzchen": "keks",
                    "gebäck": 'keks',
                    "getreide": "hafer",
                    "erdnüsse": "erdnuss",
                    "kalb": "kuh"

                },
                // emos must be sorted by lengths for better matching
                allEmos: [
                    "ei", "kuh", "eis", "lamm", "huhn", "ente", "kiwi", "mais", "pilz",
                    "brot", "käse", "taco", "salz", "dose", "reis", "keks", "wein", "bier", "schinken",
                    "fisch", "schaf", "samen", "hafer", "olive", "mango", "apfel", "birne",
                    "chili", "gurke", "salat", "breze", "pizza", "sushi", "honig", "milch",
                    "karotte", "wasser", "krabbe", "hummer", "melone", "banane", "tomate",
                    "burger", "pommes", "muffin", "kuchen", "ananas", "oktopus", "garnele", "schwein", "truthan",
                    "weintrauben", "zwiebel",
                    "paprika", "avocado", "zitrone", "kirsche", "avocado", "karotte", "steak",
                    "burrito", "spiegelei", "popcorn",
                    "schinken", "karotte", "aubergine", "erdbeere", "pfirsich", "brokkoli",
                    "erdnuss", "kastanie", "baguette", "sandwich", "cocktail",
                    "kartoffel", "knoblauch", "blaubeere", "orange", "kokosnuss", "kartoffel",
                    "croissant", "spaghetti", "reis", "schokolade",
                    "tintenfisch", "pfannkuchen", "schnittlauch",
                    "wassermelone", "süßkartoffel"
                ],
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
            shuffleArray(a) {
                for (let i = a.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [a[i], a[j]] = [a[j], a[i]];
                }
                return a;
            },
            wordToEmoji(word) {
                if (word !== "") {
                    const lowercasedWord = word.toLowerCase()
                    let matchingEmojie = ''
                    // direct search
                    if (lowercasedWord in this.allPossibleEmos) {
                        // there is a identical name in the images
                        matchingEmojie = lowercasedWord
                    } else {
                        // try to search substrings
                        if (word.length > 3) {
                            this.allPossibleEmos.forEach(emo => {
                                if (lowercasedWord.includes(emo) || emo.includes(lowercasedWord)) {
                                    matchingEmojie = emo
                                }
                            })
                        }
                    }
                    console.log(matchingEmojie)
                    if (matchingEmojie !== '') {
                        if (Object.keys(this.emoMap).includes(matchingEmojie)) matchingEmojie = this.emoMap[
                            matchingEmojie]
                        this.matchingEmos.push(matchingEmojie)
                    }
                }
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
            setupMatchinEmos() {
                let words = []
                console.log(this.recipe)
                if (!this.recipe) {
                    // load random keys as words
                    console.log("NO RECIPE")
                    this.matchingEmos = this.shuffleArray(this.allEmos)
                } else {
                    words = this.recipe.ingredients.toString().replaceAll(",", " ").split(" ")
                    words.forEach(this.wordToEmoji)

                    // if we dit not find any emojis
                    if (this.matchingEmos.length === 0) {
                        this.matchingEmos = this.shuffleArray(this.allEmos)
                    }
                    // remove all duplicates
                    this.matchingEmos = [...new Set(this.matchingEmos)];
                }

                var line = new Array(Math.floor((this.elementsInRow + 2) / this.matchingEmos.length))
                    .fill(this.matchingEmos)
                    .flat()

                var diff = this.elementsInRow - line.length + 2
                if (diff > 0) {
                    line = line.concat(this.matchingEmos.slice(0, diff))
                }
                this.reverseLine = [...line].reverse()
                this.line = line
                this.matchingEmos = []
            },
        },
        created() {
            this.emoMapKeys = Object.keys(this.emoMap)
            this.allPossibleEmos = this.allEmos.concat(this.emoMapKeys).sort(function (a, b) {
                // ASC  -> a.length - b.length
                // DESC -> b.length - a.length
                return b.length - a.length;
            });
        },
        mounted() {
            this.calculateElementsInRow()
            this.calculateNumRows()
            this.setupMatchinEmos()

            let ob = new ResizeObserver((mutationList, a) => {
                this.height = mutationList[0].target.clientHeight
                this.width = mutationList[0].target.clientWidth
            })
            ob.observe(this.$parent.$el)
        },
        watch: {
            "recipe": function () {
                this.setupMatchinEmos()
            },
            "height": function () {
                this.calculateNumRows()
            },

            "width": function () {
                this.calculateElementsInRow()
                this.setupMatchinEmos()
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