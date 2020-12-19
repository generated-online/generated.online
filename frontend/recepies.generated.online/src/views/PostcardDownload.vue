<template>
    <div  class="shady" style=" overflow: auto;">
        <Postcard :absender='query.absender' id="all"
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
    components:{
        Postcard
    },
    data(){
        return {
            query: () => {}
        }
    },
    created() {
        this.query = this.$route.query
    },
    mounted() {
        // should do this after the background is fully loaded, maybe there is an elegant way of doing this
        setTimeout(()=>{this.saveImages(); this.$router.back()},500);
    },
    methods: {
        saveImages() {
            for (let selector_name of ["postcard-front", "postcard-back"].values()){
                const el = document.querySelector('#'+selector_name)
                html2canvas(el, {
                    scrollX: 0,
                    scrollY: -window.scrollY,
                }).then(canvas => {
                    this.saveAs(canvas.toDataURL(), selector_name+'_'+this.query.recipe.id+'_'+this.query.name+'.png');
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

</style>