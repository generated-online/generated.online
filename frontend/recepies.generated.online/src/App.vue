<template>
    <v-app id="app">
<!--        <v-navigation-drawer app>
            &lt;!&ndash; &ndash;&gt;
        </v-navigation-drawer>-->

<!--        <v-app-bar app>
            &lt;!&ndash; &ndash;&gt;
        </v-app-bar>-->

        <!-- Sizes your content based upon application components -->
        <v-content >
            <!-- Provides the application the proper gutter -->
            <v-container fluid >
                <!-- If using vue-router -->
                <router-view></router-view>
            </v-container>
        </v-content>

<!--        <v-footer app>
            &lt;!&ndash; &ndash;&gt;
        </v-footer>-->
    </v-app>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.small-font {
    font-size: 0.8em  !important;
}
.normal-font {
    font-size: 1.1em  !important;
}
.large-font {
    font-size: 2em !important;
}
.red-highlight:hover {
    color: #b71c1c !important;
}
.green-highlight:hover {
    color: green !important;
}
.larger-font {
    font-size: 1.3em !important;
    line-height: 1.3em !important;
    font-weight: normal !important;
    color: #121212 !important;
}
.list {
    min-height: 28px !important;
}
.center-text {
    text-align: center !important;
}

</style>
