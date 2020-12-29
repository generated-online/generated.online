import EmojiStorage from "@/functions/emojiStorage";

let emoMapKeys = Object.keys(EmojiStorage.emoMap)
let allPossibleEmos = EmojiStorage.allEmos.concat(emoMapKeys).sort(function (a, b) {
    // ASC  -> a.length - b.length
    // DESC -> b.length - a.length
    return b.length - a.length;
});

const images = require.context('@/assets/emojies/', false, /\.png$/);


function _wordToEmoji(word, matchingEmos, replacedString=[]) {
    if (word !== "") {
        const lowercasedWord = word.toLowerCase()
        let matchingEmojie = []

        // direct search
        if (allPossibleEmos.includes(lowercasedWord)) {
            // there is a identical name in the images
            matchingEmojie.push(lowercasedWord)
        } else {
            // try to search substrings
            allPossibleEmos.forEach(emo => {
                if ((lowercasedWord.includes(emo) && emo.length > 3) || (lowercasedWord.length > 3 && emo.includes(lowercasedWord))) {
                    matchingEmojie.push(emo)
                }
            })

            // if one match is part of another (i.e. wein and schWein), take the longer one
            let sum = (c1, c2) => c1+c2
            // [wein, schwein] => [2, 1] => [false, true]
            matchingEmojie=matchingEmojie.filter(emo => Number(matchingEmojie.map(emo2 => emo2.includes(emo)).reduce(sum))===1)

        }
        if (matchingEmojie.length>0) {
            replacedString.push(...matchingEmojie)

            matchingEmojie = matchingEmojie.map((m,_) => {
                if(Object.keys(EmojiStorage.emoMap).includes(m)){
                    return EmojiStorage.emoMap[m]
                }
                return m
            })

            matchingEmos.push(...new Set(matchingEmojie))
        }
    }
}

function shuffleArray(a) {
    for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
}

export function recipeToEmojis(recipe) {
    let words = []
    let matchingEmos = [];

    if (!recipe) {
        // load random keys as words
        matchingEmos = shuffleArray(EmojiStorage.allEmos)
    } else {
        // let wordArray = [...recipe.ingredients]
        // wordArray.push(recipe.title);

        words = recipe.ingredients.toString().replaceAll(",", " ").split(" ")
        words.forEach((word) => {
            _wordToEmoji(word, matchingEmos)
        })

        // if we dit not find any emojis
        if (matchingEmos.length === 0) {
            matchingEmos = shuffleArray(EmojiStorage.allEmos)
        }
        // remove all duplicates
        matchingEmos = [...new Set(matchingEmos)];
    }
    return matchingEmos;
}

export function getEmojiLines(recipe, elementsInRow) {
    let matchingEmos = recipeToEmojis(recipe);

    var line = new Array(Math.floor((elementsInRow + 2) / matchingEmos.length))
        .fill(matchingEmos)
        .flat()

    var diff = elementsInRow - line.length + 2
    if (diff > 0) {
        line = line.concat(matchingEmos.slice(0, diff))
    }
    let reverseLine = [...line].reverse()
    return [line, reverseLine]
}
export function getImgUrl(emoji) {
    if (emoji === undefined) emoji = "knoblauch"
    return images('./' + emoji + ".png")
}

export function wordToEmoji(word){
    let emojis = []
    _wordToEmoji(word, emojis)
    return emojis.map(getImgUrl)
}

export function sentenceToEmoji(word){
    return [].concat(...word.split(" ").map(wordToEmoji))
}