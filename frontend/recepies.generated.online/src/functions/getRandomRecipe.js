import firebase from "firebase";

export async function getRandomRecipeID() {
    let db = firebase.firestore();
    const ref = db.collection("recipes")
    let key = "";

    key = ref.doc().id;
    return await ref
        .where(firebase.firestore.FieldPath.documentId(), ">=", key)
        .limit(1)
        .get()
        .then((snap) => {
            if (snap.size === 0) {
                ref
                    .where(firebase.firestore.FieldPath.documentId(), "<", key)
                    .limit(1)
                    .get()
                    .then((snap) => {
                        console.log("did not found recipe, not replacing")
                        return snap.docs[0].id
                    });
            } else {
                return snap.docs[0].id
            }
        })
        .catch((err) => {
            console.error(err)
        })
}