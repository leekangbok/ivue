// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuetify from 'vuetify'
import App from './App'
import AppAdmin from './AppAdmin'
import store from './store'
import router from './router'
import axios from 'axios'
import { iuComponentsInstall } from './components'

import ('vuetify/dist/vuetify.min.css')

Vue.use(Vuetify)
iuComponentsInstall(Vue)

Vue.prototype.$http = axios

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: {
    App,
    AppAdmin
  }
})
