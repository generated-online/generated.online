<template>
    <div class="background" :style="background+' background: var(--bg-color)'">
        <div v-for='_row in numRow' :key="_row">
            <!-- uneven rows vue starts indexing at 1 lol-->
            <div :style="row">
                <div v-if="_row % 2 == 0" :style="uneven">
                    <!-- <div :style="halfSpacer"></div> -->
                    <div class="emojie-container" :style="emojiContainer" v-for='element in elementsInRow+2'
                        :key="element">
                        <div class="emoji" :style="emoji">{{line[element-1]}}</div>
                        <!-- <div class="emoji" :style="emoji">💯{{element}}</div> -->
                    </div>
                    <!-- <div :style="halfSpacer"></div> -->
                </div>
                <!-- even rows -->
                <div v-else :style="even">
                    <div class="emojie-container" :style="emojiContainer" v-for='element in (elementsInRow+1)'
                        :key="element">
                        <div class="emoji" :style="emoji">{{reverseLine[element-1]}}</div>
                        <!-- <div class="emoji" :style="emoji">✅{{element-1}}</div> -->
                    </div>
                    <!-- {{reverseLine}} -->
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
                default: ''
            },
            "emojiContainerSize": {
                type: String,
                default: "5em"
            },
            "emojieSize": {
                type: String,
                default: "3em"
            }
        },
        data() {
            return {
                width: window.innerWidth,
                elementsInRow: 1,
                numRow: 1,
                rowMargin: "5px",
                line: [],
                reverseLine: [],
                allEmos: {
                    "Ei": "🥚",
                    "Tee": "☕",
                    "Kuh": "🐄",
                    "Eis": "🍨",
                    "Rind": "🐂",
                    "Kalb": "🐄",
                    "Lamm": "🐑",
                    "Huhn": "🐓",
                    "Ente": "🦆",
                    "Rose": "🌹",
                    "Kiwi": "🥝",
                    "Mais": "🌽",
                    "Pilz": "🍄",
                    "Brot": "🍞",
                    "Käse": "🧀",
                    "Taco": "🌮",
                    "Salz": "🧂",
                    "Dose": "🥫",
                    "Reis": "🍚",
                    "Keks": "🍪",
                    "Wein": "🍷",
                    "Bier": "🍺",
                    "Brühe": "🥘",
                    "Speck": "🥓",
                    "Lachs": "🐟",
                    "Fisch": "🐟",
                    "Schaf": "🐏",
                    "Samen": "🌱",
                    "Hafer": "🌾",
                    "Olive": "🫒",
                    "Mango": "🥭",
                    "Apfel": "🍎",
                    "Äpfel": "🍎",
                    "Birne": "🍐",
                    "Chili": "🌶",
                    "Gurke": "🥒",
                    "Salat": "🥗",
                    "Breze": "🥨",
                    "Bagel": "🥯",
                    "Speck": "🥓",
                    "Pizza": "🍕",
                    "Sushi": "🍱",
                    "Honig": "🍯",
                    "Milch": "🥛",
                    "Suppe": "🍵",
                    "Spieß": "🍡",
                    "Möhre": "🥕",
                    "Eigelb": "🥚",
                    "Wasser": "💧",
                    "Krabbe": "🦀",
                    "Hummer": "🦞",
                    "Melone": "🍈",
                    "Banane": "🍌",
                    "Tomate": "🍅",
                    "Gemüse": "🥬",
                    "Burger": "🍔",
                    "Pommes": "🍟",
                    "Knödel": "🥟",
                    "Muffin": "🧁",
                    "Kuchen": "🎂",
                    "Ananas": "🍍",
                    "Kräuter": "🌿",
                    "Thymian": "🍃",
                    "Oregano": "🍃",
                    "Oktopus": "🐙",
                    "Garnele": "🦐",
                    "Schwein": "🐖",
                    "Truthan": "🦃",
                    "Kräuter": "🌿",
                    "Trauben": "🍇",
                    "Zwiebel": "🧅",
                    "Paprika": "🫑",
                    "Avocado": "🥑",
                    "Zitrone": "🍋",
                    "Kirsche": "🍒",
                    "Avocado": "🥑",
                    "Karotte": "🥕",
                    "Fleisch": "🥩",
                    "Hot Dog": "🌭",
                    "Burrito": "🌯",
                    "Spiegei": "🍳",
                    "Popcorn": "🍿",
                    "Krapfen": "🍩",
                    "Pudding": "🍮",
                    "Flasche": "🍶",
                    "Flasche": "🍾",
                    "Parmesan": "🧀",
                    "Schinken": "🥓",
                    "Hähnchen": "🐓",
                    "Karrotte": "🥕",
                    "Obergine": "🍆",
                    "Erdbeere": "🍓",
                    "Pfirsich": "🍑",
                    "Erdbeere": "🍓",
                    "Brokkoli": "🥦",
                    "Erdnüsse": "🥜",
                    "Kastanie": "🌰",
                    "Baguette": "🥖",
                    "Sandwich": "🥪",
                    "Schüssel": "🥣",
                    "Cocktail": "🍸",
                    "Basilikum": "🌱",
                    "Kartoffel": "🥔",
                    "Knoblauch": "🧄",
                    "Blaubeere": "🫐",
                    "Mandarine": "🍊",
                    "Kokosnuss": "🥥",
                    "Aubergine": "🍆",
                    "Kartoffel": "🥔",
                    "Croissant": "🥐",
                    "Spaghetti": "🍝",
                    "Petersilie": "🌿",
                    "Haselnüsse": "🌰",
                    "Curry-Reis": "🍛",
                    "Glückskeks": "🥠",
                    "Schokolade": "🍫",
                    "Gemüsebrühe": "🥘",
                    "Champignons": "🍄",
                    "Tintenfisch": "🦑",
                    "Sonnenblume": "🌻",
                    "Pfannkuchen": "🥞",
                    "Schnittlauch": "🎋",
                    "Wassermelone": "🍉",
                    "Süßkartoffel": "🍠",
                },
                matchingEmos: []
            }
        },
        methods: {
            getRandomNumber(min, max) {
                return Math.random() * (max - min) + min;
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
                    const capitalizedWord = lowercasedWord.replace(/^\w/, c => c.toUpperCase());

                    if (capitalizedWord in this.allEmos) {
                        // isMatching = true
                        const matchingEmojie = this.allEmos[capitalizedWord]
                        this.matchingEmos.push(matchingEmojie)
                    } else {
                        if (word.length > 3) {
                            let matchingEmojie = ''
                            for (const key in this.allEmos) {
                                if (lowercasedWord.includes(key.toLowerCase()) || key.toLowerCase().includes(
                                        lowercasedWord)) {
                                    matchingEmojie = this.allEmos[key]
                                }
                            }
                            // Take last match
                            if (matchingEmojie !== '') {
                                this.matchingEmos.push(matchingEmojie)
                            }
                        }
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
                if (this.recipe === '') {
                    // load random keys as words
                    words = this.shuffleArray(Object.keys(this.allEmos))
                } else {
                    words = this.recipe.ingredients.toString().replaceAll(",", " ").split(" ")
                }
                words.forEach(this.wordToEmoji)

                // if we dit not find any emojis
                if (this.matchingEmos.length == 0) {
                    words = this.shuffleArray(Object.keys(this.allEmos))
                    words.forEach(this.wordToEmoji)
                }

                // remove all duplicates
                this.matchingEmos = [...new Set(this.matchingEmos)];

                var line = new Array(Math.floor((this.elementsInRow + 2) / this.matchingEmos.length)).fill(this
                        .matchingEmos)
                    .flat();

                var diff = this.elementsInRow - line.length + 2
                if (diff > 0) {
                    line = line.concat(this.matchingEmos.slice(0, diff))
                }
                this.reverseLine = [...line].reverse()
                this.line = line
                this.matchingEmos = []
            },

        },

        mounted() {

            this.calculateElementsInRow()
            this.calculateNumRows()
            this.setupMatchinEmos()

            window.addEventListener('resize', () => {
                this.calculateElementsInRow()
                this.calculateNumRows()
                this.setupMatchinEmos()

            })
        },
        computed: {
            emojiContainer() {
                var d = {
                    "height": this.emojiContainerSize,
                    "width": this.emojiContainerSize,
                }
                return this.dictToCssString(d)
            },
            emoji() {
                var d = {
                    "font-size": this.emojieSize,
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
            background() {
                return this.dictToCssString({
                    "margin-top": "-" + this.emToPixle(this.emojiContainerSize) / 2 + "px",
                    "margin-bottom": "-" + this.emToPixle(this.emojiContainerSize) / 2 + "px",
                    // "margin-right": -this.rowMargin
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
        /* opacity: 0.8; */
    }

    .emojie-container {
        opacity: 0.2;
        float: left;
        /* width: 4em;
        height: 4em; */
        text-align: center;
        display: table;
    }

    .emoji {
        /* font-size: 3em; */
        display: table-cell;
        vertical-align: middle;
    }
</style>