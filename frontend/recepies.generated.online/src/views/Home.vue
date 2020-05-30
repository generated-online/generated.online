<template>
  <div class="home">
    <h1 class="title">EAT AI FOOD</h1>
  <div>
    <div v-for="recepie in recepies" :key="recepies.id" class="recipieContainer">
      <h2 class="recipieTitle">{{recepie.title}}</h2>
      <div class="intigrentsContainer">
        <ul style="list-style-type:none;">
          <li v-for="intigrent in recepie.intrigents">{{intigrent}}</li>
        </ul>
      </div>
      <div class="recipieInstructions">{{recepie.instructions}}</div>
    </div>
  </div>

    <div class="footer">
      <ul>
        <li>About</li>
        <li><a href="https://github.com/generated-online"><img src="/github.png" alt="" >GitHub</a></li>
      </ul>
    </div>
  </div>
</template>

<script>

import firebase from "firebase";

export default {
  name: 'home',
  components: {
  },
  data() {
    return {
      recepies: [],
    }
  },
  created() {
    let db = firebase.firestore();
    let potholeRef = db
            .collection("firstTest")
            .get()
            .then(snap => {
              snap.docs.map(doc => {
                if (doc.data().title !== '') {
                  this.recepies.push({
                    id: doc.title,
                    intrigents: doc.data().intrigents,
                    title: doc.data().title,
                    instructions: doc.data().instructions
                  });
              }
              });
            })
            .catch(err => {
              console.log('Error getting document', err)
            });
  },
}
</script>

<style>
  .title {
    padding: 1em;
    background: #2c3e50;
    color: #ECEFF1;
    font-size: 3em;
  }

  .footer li {
    display: inline-block;
    margin-left: 1em;
  }
  .footer {
    background: #2c3e50;
    position: fixed;
    padding-top: 30px;
    padding-bottom: 30px;
    left: 0;
    bottom: 0;
    width: 100%;
    color: white;
    text-align: center;
  }
  .item {
    align-content: ;
    margin: 1em;
    padding: 1em;
    text-decoration: none;
    font-size: 2em;
    border-style: groove;
    border-radius: 100px;
    border-color: black;
    color: black;
    display: inline-block;
    transition: 0.5s;
  }
  .item:hover {
    background: #5c6bc0;
    color: #ECEFF1;
  }

  li img {
    width: 32px;
    bottom: 0;
    vertical-align:middle
  }
  a:visited {
    color: black
  }

  .item-collection {
    overflow: auto;
    margin: 0 auto;
  }
  .recipieTitle {
    color: #ECEFF1;
    background-color: #2c3e50;
  }

  .recipieInstructions {
  text-align: justify;
    padding: 20%;
    padding-top: 20px;
    padding-bottom: 20px;
  }

.intigrentsContainer {
  padding: 20px;
  font-style: oblique;
  font-family: "Andale Mono";
}

  /* Pattern styles */
  .recipieContainer {
    display: table;
    width: 100%;
    height: 100%;
    padding: 60px;
  }

  .left-half {
    position: absolute;
    left: 0px;
    width: 50%;
  }

  .right-half {
    position: absolute;
    right: 0px;
    width: 50%;
  }
</style>
