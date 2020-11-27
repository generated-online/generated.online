<template>
    <div class="background">
        <span class="emojie-batch">
            <div class="emojie" v-for="(e, idx) in matchingEmos" :key="idx"
                :style='emojiCss + " " + ((Math.floor(idx/emojieAmount) % 2 === 0) ? "padding-left: "+emojiPadding+"; text-align: right" : "")'>
                {{e}}</div>
        </span>
    </div>
</template>

<script>
    export default {
        props: {
            "recipe": {
                type: Object,
                default: ''
            },
            "rowHeight": {
                type: String,
                default: "1.25em"
            },
            "emojieSize": {
                type: Number,
                default: 2
            },
            "emojieAmount": {
                type: Number,
                default: 30
            },
            "emojiPadding": {
                type: String,
                default: "0.65em"
            }

        },
        data() {
            return {
                width: window.innerWidth,
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
            }
        },
        created() {
            let words = []
            if (this.recipe === '') {
                // load random keys as words
                words = this.shuffleArray(Object.keys(this.allEmos))
            } else {
                words = this.recipe.ingredients.toString().replaceAll(",", " ").split(" ")
            }

            words.forEach(word => {
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
            })

            // remove all duplicates
            this.matchingEmos = [...new Set(this.matchingEmos)];

            var line = new Array(Math.floor(this.emojieAmount / this.matchingEmos.length)).fill(this.matchingEmos)
                .flat();

            var diff = this.emojieAmount - line.length
            if (diff > 0) {
                line = line.concat(this.matchingEmos.slice(0, diff))
            }
            this.reverseLine = [...line].reverse()
            this.line = line
            this.matchingEmos = []
        },
        mounted() {
            var height = this.$parent.$el.offsetHeight;
            var em = parseFloat(getComputedStyle(this.$parent.$el).fontSize);

            var rowHeightInPx = parseFloat(this.rowHeight) * em * this.emojieSize;
            var numRows = Math.floor(height / rowHeightInPx);

            // this.matchingEmos
            var i;
            for (i = 0; i < numRows; i++) {
                this.matchingEmos = this.matchingEmos.concat(i % 2 ? this.line : this.reverseLine)
            }

            window.addEventListener('resize', () => {
                // in the paypal button rendering we trigger this
                height = this.$parent.$el.offsetHeight;
                var newNumRows = Math.floor(height / rowHeightInPx);

                var i;
                // add new rows depending on the difference in hight
                for (i = 0; i < newNumRows - numRows; i++) {
                    this.matchingEmos = this.matchingEmos.concat(i % 2 ? this.line : this.reverseLine)
                }

            })
        },
        computed: {
            emojiCss() {
                var d = {
                    "height": this.rowHeight,
                    "font-size": this.emojieSize + "em",
                    "width": 100 / this.emojieAmount + "%",
                }
                // this generates correct css string out of object
                var s = ""
                for (var key in d) {
                    s += key + ": " + d[key] + "; "
                }
                return s
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
    }

    .emojie-batch {
        width: 100vw;
    }

    .emojie {
        opacity: 0.3;
        float: left;
    }
</style>