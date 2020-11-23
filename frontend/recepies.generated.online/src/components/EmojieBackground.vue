<template>
    <div class="background">
        <span class="emojie-batch">
            <div class="emojie" v-for="(e, idx) in matchingEmos" :key="idx"
                :style='emojiCss + " " + (Math.floor(idx/emojieAmount) % 2 === 0) ? "padding-left: 3px; text-align: right" : "" '>
                {{e}}</div>
        </span>
    </div>
</template>

<script>
    export default {
        props: {
            "recipe": {
                type: Object,
                default: {}
            },
            "rowHeight": {
                type: String,
                default: "70px"
            },
            "emojieSize": {
                type: String,
                default: "2em"
            },
            "emojieAmount": {
                type: Number,
                default: 4
            },

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
                    "Fisch": "🐟",
                    "Schaf": "🐏",
                    "Samen": "🌱",
                    "Hafer": "🌾",
                    "Olive": "🫒",
                    "Mango": "🥭",
                    "Apfel": "🍎",
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
                    "Annanas": "🍍",
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
                    "Kartoffel": "🥔",
                    "Knoblauch": "🧄",
                    "Blaubeere": "🫐",
                    "Mandarine": "🍊",
                    "Kokosnuss": "🥥",
                    "Aubergine": "🍆",
                    "Kartoffel": "🥔",
                    "Croissant": "🥐",
                    "Spaghetti": "🍝",
                    "Haselnüsse": "🌰",
                    "Curry-Reis": "🍛",
                    "Glückskeks": "🥠",
                    "Schokolade": "🍫",
                    "Tintenfisch": "🦑",
                    "Sonnenblume": "🌻",
                    "Pfannkuchen": "🥞",
                    "Wassermelone": "🍉",
                    "Süßkartoffel": "🍠",
                },
                matchingEmos: []
            }
        },
        methods: {
            getRandomNumber(min, max) {
                return Math.random() * (max - min) + min;
            }
        },
        created() {
            const words = this.recipe.ingredients.toString().replaceAll(",", " ").split(" ")
            words.forEach(word => {
                if (word !== "") {
                    const lowercasedWord = word.toLowerCase()
                    const capitalizedWord = lowercasedWord.replace(/^\w/, c => c.toUpperCase());

                    if (capitalizedWord in this.allEmos) {
                        // isMatching = true
                        const matchingEmojie = this.allEmos[capitalizedWord]
                        this.matchingEmos.push(matchingEmojie)
                    } else {
                        if (word.length >= 2) {
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
            // for (i in 10) {
            this.matchingEmos = this.matchingEmos.concat(this.matchingEmos)
            this.matchingEmos = this.matchingEmos.concat(this.matchingEmos)
            this.matchingEmos = this.matchingEmos.concat(this.matchingEmos)
            this.matchingEmos = this.matchingEmos.concat(this.matchingEmos)
            this.matchingEmos = this.matchingEmos.concat(this.matchingEmos)
            this.matchingEmos = this.matchingEmos.concat(this.matchingEmos)
            this.matchingEmos = this.matchingEmos.concat(this.matchingEmos)
            this.matchingEmos = this.matchingEmos.concat(this.matchingEmos)
            this.matchingEmos = this.matchingEmos.concat(this.matchingEmos)
            this.matchingEmos = this.matchingEmos.concat(this.matchingEmos)
            this.matchingEmos = this.matchingEmos.concat(this.matchingEmos)
            this.matchingEmos = this.matchingEmos.concat(this.matchingEmos)
            // }
        },
        computed: {
            emojiCss() {
                return {
                    "height": this.rowHeight,
                    "font-size": this.emojieSize,
                    "width": 100 / this.emojieAmount + "%",
                }
            }
        }
    }
</script>

<style scoped>
    .background {
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
        opacity: 0.6;
        float: left;
    }
</style>