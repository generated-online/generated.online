<template>
    <div id="app">
        <v-app id="inspire">
            <router-view :key="$route.path"></router-view>
        </v-app>
    </div>
</template>