import Vue from 'vue'
import Vuex from 'vuex'
import * as actions from './actions'
import * as getters from './getters'
import SidebarMenu from './modules/sidebar-menu'
import Cart from './modules/cart'

Vue.use(Vuex)

export default new Vuex.Store({
  actions,
  getters,
  modules: {
    SidebarMenu,
    Cart
  }
})
