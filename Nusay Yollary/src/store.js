// store.js
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    changeLang: 'tk'
  },
  mutations: {
    setchangeLang(state, language) {
      state.changeLang= language;
    }
  }
});
