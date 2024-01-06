import { createApp } from 'vue'
import i18n from './plugins/i18n'
import {createI18n} from 'vue-i18n'
import i18next from "i18next";
import I18NextVue from "i18next-vue";
import './style.css'
import App from './App.vue'
import './assets/global.css'
import Splide from '@splidejs/vue-splide';
import router from './router'

import { OhVueIcon, addIcons } from "oh-vue-icons";
import { FaFlag, RiZhihuFill } from "oh-vue-icons/icons";
// import FontAwesomeIcon from '@fortawesome/vue-fontawesome'
import '@splidejs/vue-splide/css/skyblue';
import '@splidejs/vue-splide/css/sea-green'
import "@splidejs/splide/dist/css/themes/splide-default.min.css";

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faUserSecret)
// Vue.config.productionTip = true



const app = createApp(App)
app.use(router)
// app.use(VueSplide)
app.component('font-awesome-icon', FontAwesomeIcon)
app.component("v-icon", OhVueIcon);
app.use(i18n)
app.mount('#app')
// app.use(i18next)
// app.use(I18NextVue)
app.use(Splide)
