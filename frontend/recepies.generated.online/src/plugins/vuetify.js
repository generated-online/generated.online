import Vue from 'vue';
import Vuetify from 'vuetify/lib';
//import colors from 'vuetify/es5/util/colors'

Vue.use(Vuetify)


export default new Vuetify({
  icons: {
    iconfont: 'mdi',
  },
  theme: {
    themes: {
      light: {
        primary: '#3f51b5',
            secondary: '#f7f6f9',
            accent: '#8c9eff',
            error: '#b71c1c',
          //
              GOdark: "#323E40",
              GOgrey: "#939ca8",
              GOyellow: "#F2AB27",
              GOorange: "#D97D0D",
              GOdarkred: "#732002",
              GOred: "#D94D1A",
      },
    },
  },
});
