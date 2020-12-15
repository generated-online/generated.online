import EmojiStorage from "@/functions/emojiStorage";

let emoMapKeys = Object.keys(EmojiStorage.emoMap)
let allPossibleEmos = EmojiStorage.allEmos.concat(emoMapKeys).sort(function (a, b) {
    // ASC  -> a.length - b.length
    // DESC -> b.length - a.length
    return b.length - a.length;
});

function wordToEmoji(word, matchingEmos) {
    if (word !== "") {
        const lowercasedWord = word.toLowerCase()
        let matchingEmojie = ''
        // direct search
        if (lowercasedWord in allPossibleEmos) {
            // there is a identical name in the images
            matchingEmojie = lowercasedWord
        } else {
            // try to search substrings
            if (word.length > 3) {
                allPossibleEmos.forEach(emo => {
                    if (lowercasedWord.includes(emo) || emo.includes(lowercasedWord)) {
                        matchingEmojie = emo
                    }
                })
            }
        }
        if (matchingEmojie !== '') {
            if (Object.keys(EmojiStorage.emoMap).includes(matchingEmojie)) matchingEmojie = EmojiStorage.emoMap[
                matchingEmojie]
            matchingEmos.push(matchingEmojie)
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
            wordToEmoji(word, matchingEmos)
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
export function getImgUrl(emojie) {
    if (emojie === undefined) emojie = "knoblauch"

    var images = require.context('@/assets/emojies/', false, /\.png$/)
    return images('./' + emojie + ".png")
}