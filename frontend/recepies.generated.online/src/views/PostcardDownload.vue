<template>
    <div class="shady" style="overflow: auto;">
        <Postcard class="shady" :absender='query.absender'
                  :country='query.country'
                  :horizontal="false"
                  :name='query.name'
                  :parent-width="1440"
                  :recipe='query.recipe'
                  :street='query.street'
                  :zip='query.zip' id="correctPostcard"/>
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
    props:["query"],
    methods: {
        async saveImages() {
            for (let selector_name of ["postcard-front", "postcard-back"].values()) {
                const postcardPart = document.querySelector("#correctPostcard #" + selector_name)
                await html2canvas(postcardPart, {
                    scrollX: 0,
                    scrollY: -window.scrollY,
                }).then(canvas => {
                    // document.body.appendChild(canvas);
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