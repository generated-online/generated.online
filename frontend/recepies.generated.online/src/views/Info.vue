<template>
    <v-card class="info-container">
        <v-container :class="['mb-16',{'mt-8': $vuetify.breakpoint.mdAndUp}]">
            <h1 class=text-span style="font-size:3em">Was ist das hier?</h1>
            <br>
            <h2 class="project-description">
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
                Wenn dich unser Code interessiert schau doch mal auf unserem
                <v-btn class="black-button" href="https://github.com/generated-online/generated.online">
                    <v-icon class="mr-2" size="30"> mdi-github </v-icon> Github-Repo
                </v-btn>
                vorbei und lass einen Stern da!
            </span>
            </h2>
        </v-container>
    </v-card>
</template>

<script>
import EmojieBackground from "@/components/EmojieBackground"

export default {
    components: {
        EmojieBackground
    },
    name: "info",
    created() {
        this.$emit('shareText', "Schau dir diese coolen von einer KI generierten Rezepte an!");
        this.$emit('recipe', null);
    }
};
</script>

<style scoped>

.project-description {
    text-align: justify;
    margin-bottom: 1em;
}
</style>