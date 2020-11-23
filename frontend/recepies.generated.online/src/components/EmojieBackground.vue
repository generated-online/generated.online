<template>
    <div class="background">

        <span class="emojie" v-for="(e, idx) in matchingEmos" v-bind:key="idx"
            :style="'top:'+ e.top + 'px; left:' + e.left +'px;'">{{e.text}}</span>
    </div>
</template>

<script>
    export default {
        props: ["recipe"],
        data() {
            return {
                allEmos: {
                    "Wasser": ["💧"],
                    "Fisch": ["🐳", "🐬", "🐋", "🐟", "🐠", "🦈"],
                    "Oktopus": ["🐙"],
                    "Krabbe": ["🦀"],
                    "Hummer": ["🦞"],
                    "Garnele": ["🦐"],
                    "Tintenfisch": ["🦑"],
                    "Kuh": ["🐮", "🐄", "🐂"],
                    "Rind": ["🐮", "🐄", "🐂"],
                    "Kalb": ["🐮", "🐄", "🐂"],
                    "Schwein": ["🐖", "🐷", "🐽"],
                    "Schaf": ["🐏", "🐑"],
                    "Lamm": ["🐏", "🐑"],
                    "Truthan": ["🦃"],
                    "Huhn": ["🐔", "🐓"],
                    "Hähnchen": ["🐔", "🐓"],
                    "Ente": ["🦆"],
                    "Rose": ["🌹"],
                    "Sonnenblume": ["🌻"],
                    "Samen": ["🌱"],
                    "Hafer": ["🌾"],
                    "Kräuter": ["🌿"],
                    "Trauben": ["🍇"],
                    "Melone": ["🍈"],
                    "Kartoffel": ["🥔"],
                    "Zwiebel": ["🧅"],
                    "Knoblauch": ["🧄"],
                    "Olive": ["🫒"],
                    "Karrotte": ["🥕"],
                    "Paprika": ["🫑"],
                    "Avocado": ["🥑"],
                    "Obergine": ["🍆"],
                    "Blaubeere": ["🫐"],
                    "Erdbeere": ["🍓"],
                    "Wassermelone": ["🍉"],
                    "Mandarine": ["🍊"],
                    "Zitrone": ["🍋"],
                    "Banane": ["🍌"],
                    "Annanas": ["🍍"],
                    "Mango": ["🥭"],
                    "Apfel": ["🍎", "🍏"],
                    "Birne": ["🍐"],
                    "Pfirsich": ["🍑"],
                    "Kirsche": ["🍒"],
                    "Erdbeere": ["🍓"],
                    "Kiwi": ["🥝"],
                    "Tomate": ["🍅"],
                    "Kokosnuss": ["🥥"],
                    "Avocado": ["🥑"],
                    "Aubergine": ["🍆"],
                    "Kartoffel": ["🥔"],
                    "Karotte": ["🥕"],
                    "Mais": ["🌽"],
                    "Chili": ["🌶"],
                    "Gurke": ["🥒"],
                    "Salat": ["🥬", "🥗"],
                    "Brokkoli": ["🥦"],
                    "Pilz": ["🍄"],
                    "Erdnüsse": ["🥜"],
                    "Haselnüsse": ["🌰"],
                    "Kastanie": ["🌰"],
                    "Brot": ["🍞"],
                    "Croissant": ["🥐"],
                    "Baguette": ["🥖"],
                    "Breze": ["🥨"],
                    "Bagel": ["🥯"],
                    "Pfannkuchen": ["🥞"],
                    "Käse": ["🧀"],
                    "Fleisch": ["🥩"],
                    "Speck": ["🥓"],
                    "Burger": ["🍔"],
                    "Pommes": ["🍟"],
                    "Pizza": ["🍕"],
                    "Hot Dog": ["🌭"],
                    "Sandwich": ["🥪"],
                    "Taco": ["🌮"],
                    "Burrito": ["🌯"],
                    "Ei": ["🥚"],
                    "Spiegei": ["🍳"],
                    "Topf mit Lebensmitteln": ["🥘", "🍲", "🥙", "🍜"],
                    "Schüssel": ["🥣"],
                    "Popcorn": ["🍿"],
                    "Salz": ["🧂"],
                    "Dose": ["🥫"],
                    "Sushi": ["🍱", "🍣"],
                    "Reis": ["🍚"],
                    "Curry-Reis": ["🍛"],
                    "Spaghetti": ["🍝"],
                    "Süßkartoffel": ["🍠"],
                    "Spieß": ["🍢", "🍡"],
                    "Knödel": ["🥟"],
                    "Glückskeks": ["🥠"],
                    "Eis": ["🍨", "🍧", "🍦"],
                    "Krapfen": ["🍩"],
                    "Keks": ["🍪"],
                    "Muffin": ["🧁"],
                    "Kuchen": ["🥧", "🍰", "🎂", "🥮"],
                    "Schokolade": ["🍫"],
                    "Süßigkeiten": ["🍬", "🍭"],
                    "Pudding": ["🍮"],
                    "Honig": ["🍯"],
                    "Milch": ["🥛"],
                    "Tee": ["☕"],
                    "Suppe": ["🍵"],
                    "Flasche": ["🍶"],
                    "Flasche": ["🍾"],
                    "Wein": ["🍷"],
                    "Cocktail": ["🍸", "🍹", "🥂"],
                    "Bier": ["🍺", "🍻", "🥃"],
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
            var winWidth = window.innerWidth;
            var winHeight = window.innerHeight;

            const words = this.recipe.ingredients.toString().replaceAll(",", " ").split(" ")
            words.forEach(word => {
                if (word !== "") {
                    const lowercasedWord = word.toLowerCase()
                    const capitalizedWord = lowercasedWord.replace(/^\w/, c => c.toUpperCase());

                    // random position
                    const randomTop = this.getRandomNumber(0, winHeight);
                    const randomLeft = this.getRandomNumber(0, winWidth);

                    if (capitalizedWord in this.allEmos) {
                        // isMatching = true
                        let matchingEmoArray = this.allEmos[capitalizedWord]
                        const matchingEmojie = matchingEmoArray[Math.floor(Math.random() * matchingEmoArray
                            .length)]
                        this.matchingEmos.push({
                            "text": matchingEmojie,
                            "top": randomTop,
                            "left": randomLeft
                        })
                    } else {
                        if (word.length >= 4) {
                            for (const key in this.allEmos) {
                                if (lowercasedWord.includes(key.toLowerCase()) || key.toLowerCase().includes(
                                        lowercasedWord)) {
                                    // isMatching = true
                                    let matchingEmoArray = this.allEmos[key]
                                    const matchingEmojie = matchingEmoArray[Math.floor(Math.random() *
                                        matchingEmoArray
                                        .length)]
                                    this.matchingEmos.push({
                                        "text": matchingEmojie,
                                        "top": randomTop,
                                        "left": randomLeft
                                    })
                                    break
                                }
                            }
                        }
                    }
                }
            })
        }

    }
</script>

<style scoped>
    .background {
        z-index: 0;
    }

    .emojie {
        font-size: 4em;
    }
</style>