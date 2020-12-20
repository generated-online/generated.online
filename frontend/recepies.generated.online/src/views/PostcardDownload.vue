<template>
    <div class="shady" style="overflow: auto;">
        <v-row align="center" justify="center" class="center">
            <v-col>
                <v-row align="center" class="loadingBox shady" no-gutters>
                    <v-col cols="auto" class="ma-1">
                        <v-progress-circular class="loading" size="40" color="black" indeterminate></v-progress-circular>
                    </v-col>
                    <v-col cols="auto" class="ma-1">
                        {{ loadingText }}
                    </v-col>
                </v-row>
            </v-col>
        </v-row>
        <Postcard class="shady" :absender='query.absender'
                  :country='query.country'
                  :horizontal="false"
                  :name='query.name'
                  :parent-width="1440"
                  :recipe='query.recipe'
                  :street='query.street'
                  :zip='query.zip'/>
    </div>
</template>

<script>
import Postcard from "@/components/postcard-stuff/Postcard";
import html2canvas from "html2canvas";

export default {
    name: "PostcardDownload",
    components: {
        Postcard
    },
    data() {
        return {
            loadingText: "Erstelle Bilder",
            query: () => {
            }
        }
    },
    created() {
        this.query = this.$route.query
    },
    mounted() {
        // should do this after the background is fully loaded, maybe there is an elegant way of doing this
        setTimeout(() => {
            this.loadingText = "Download gestartet"
            this.saveImages();
            // this is just for visual purposes
            setTimeout(() => {this.$router.back()}, 1000)
        }, 250);
    },
    methods: {
        async saveImages() {
            for (let selector_name of ["postcard-front", "postcard-back"].values()) {
                const postcardPart = document.querySelector('#' + selector_name)
                await html2canvas(postcardPart, {
                    scrollX: 0,
                    scrollY: -window.scrollY,
                }).then(canvas => {
                    this.saveAs(canvas.toDataURL(), selector_name + '_' + this.query.recipe.id + '_' + this.query.name + '.png');
                });
            }
        },
        saveAs(uri, filename) {
            var link = document.createElement('a');
            if (typeof link.download === 'string') {
                link.href = uri;
                link.download = filename;
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            } else {
                window.open(uri);
            }
        }
    }
}
</script>

<style scoped>
.loadingBox {
    margin: auto;
    padding: 2px;
    width: fit-content;
    border-radius: 50px;
    box-shadow: 0 0 10px rgba(128, 128, 128, 0.8);
    background: rgba(228, 228, 228, 0.9);
    color:black;
}
.center{
    height:100vh;
    width: 100vw;
    position: fixed;
    z-index: 100;
    left: 0;
    top: 0;
    margin: auto;
}

</style>