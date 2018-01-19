// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuetify from 'vuetify'
import App from './App'
import AppShop from './AppShop'
import store from './store'
import router from './router'
import Iu from './components'

import ('vuetify/dist/vuetify.min.css')

Vue.use(Vuetify)

Vue.use(Iu)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<AppShop/>',
  components: {
    App,
    AppShop
  }
})
