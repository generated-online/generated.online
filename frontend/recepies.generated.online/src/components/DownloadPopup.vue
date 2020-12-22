<template>
    <v-row justify="center">
        <v-dialog
                v-model="show"
                content-class="noBoxShadow"
                persistent
                width="600px"
                @input="updateShowDialog"
        >
            <v-card class="boldy" dark>
                <v-card-title>
                    <span class="headline">Willst du die Postkarten als Bilder downloaden?</span>
                </v-card-title>
                <v-spacer></v-spacer>
                <v-card-text class="text-justify">
                    Falls ja, kann es sein, dass du gefragt wirst ob es uns erlauben willst
                    Daten auf deinem Gerät zu speichern.
                    Der Download kann einen Moment dauern.
                </v-card-text>
                <v-card-text class="text-justify">
                    <b>Übrigens:</b> Die Daten die du auf unserer Website eingibts werden auch auf den Bildern mit
                    angezeigt.
                    Wie zum Beispiel Anschrift des Empfängers, oder dein Name (Absender).
                </v-card-text>
                <v-card-text>
                    <v-progress-linear
                            v-show="downloading"
                            color="var(--bg-color)"
                            indeterminate
                    ></v-progress-linear>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                            :disabled="downloading"
                            class="boldy-red"
                            text
                            @click="updateShowDialog(false)"
                    >
                        <v-icon class="my-1">close</v-icon>
                    </v-btn>
                    <v-btn
                            :disabled="downloading"
                            absolute
                            class="boldy-color"
                            left
                            style="background: green !important"
                            text
                            @click="startDownload()"
                    >
                        <v-icon class="my-1">download</v-icon>
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <PostcardDownload ref="postcardDownload" :query="query" class="hidden"/>
    </v-row>
</template>

<script>
import PostcardDownload from "@/views/PostcardDownload";

export default {
    name: "DownloadPopup",
    components: {
        PostcardDownload
    },
    props: ["showDialog", "query"],
    data() {
        return {
            show: this.showDialog,
            downloading: false
        }
    },
    methods: {
        updateShowDialog(isVisible) {
            if (isVisible) return false;
            this.$emit('update:showDialog', false)
        },
        startDownload() {
            this.downloading = true
            this.$refs.postcardDownload.saveImages().then(() => this.updateShowDialog(false))
        }
    },
}
</script>

<style scoped>
.hidden {
    width: 0;
    height: 0
}
</style>