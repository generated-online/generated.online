<template>
    <div class="info-container">
        <h1><span class=text-span>Um was geht es bei dieser Website?</span></h1>
        <br>
        <div class="project-description">
            <span class=text-span>
                Stell dir vor jemand schaut sich alle Rezepte von chefkoch.de an,
                filtert alle unbedeutenten und schlechten Rezepte raus und erstellt
                neue Rezepte basierend auf diesem Datensatz.
            </span>
            <br>
            <br>
            <span class=text-span>
                Genau das haben wir gemacht!
            </span>
            <br>
            <br>
            <span class=text-span>
                Aber anstatt uns selber neue Rezepte zu
                überlegen, haben wir eine Künstliche Intelligenz (<b>KI</b>) darauf trainiert
                möglichst gute Rezepte zu generieren.
            </span>
            <br>
            <br>
            <span class=text-span>
                Die Ergebnisse reichen von sehr lustig oder unkochbar zu einwandfrei
                vorstellbar als Rezept aus einem Kochbuch.
            </span>
            <br>
            <br>
            <span class=text-span>
                Wenn dich unser Code interessiert schau doch mal auf unserem Github-Repo vorbei und lass einen Stern da:
            </span>
        </div>
        <div class="github-button">
            <v-btn icon outlined large href="https://github.com/generated-online/generated.online">
                <v-icon class="vue-icon" align="middle" size="40">mdi-github</v-icon>
            </v-btn>
        </div>
    </div>
</template>

<script>
    export default {
        name: "info",
        created() {
            this.$emit('shareText', "Schau dir diese coolen von einer KI generierten Rezepte an!");
            this.$emit('recipeId', null);
        }
    };
</script>

<style scoped>
    .info-container {
        text-align: left;
        height: 100% !important;
        padding: 2em 2em 2em 2em;
        max-width: 100vw !important;
        min-height: 100vh !important;
        margin: 0 0 25px 0;
    }

    .project-description {
        text-align: justify;
        margin-bottom: 1em;
    }

    .github-button {
        text-align: center;
        margin-bottom: 1em
    }
</style>