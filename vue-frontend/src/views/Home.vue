<template>
  <div class="home">
    <h1 class="title">COMPLETELY AI GENERATED</h1>
    <div class="item-collection">
      <a class="item" href="https://recipes.generated.online"> 🍰 Recipes</a>
      <a class="item" href="https://recipes.generated.online"> 👨‍ Names</a>
      <a class="item" href="https://recipes.generated.online"> 👨‍👨‍👧‍👦 Siblings</a>
      <a class="item" href="https://recipes.generated.online"> 📓 Laws</a>
      <a class="item" href="https://recipes.generated.online"> ⛩ Religious Texts</a>

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


export default {
  name: 'home',
  components: {

  }
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
</style>
