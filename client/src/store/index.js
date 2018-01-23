import Vue from 'vue'
import Vuex from 'vuex'
import menu from './modules/menu'
import doctorMember from './modules/doctor/member'
import edent from './modules/edent'
import bitcoin from './modules/bitcoin'
import rioShop from './modules/rioShop'
import types from './mutation-types'

Vue.use(Vuex)

const state = {
  [types.SIDENAV_DRAWER]: null,
  [types.LOGIN_STATUS]: false,
  [types.CART_ITEMS]: [],
  [types.SHOW_LOADING]: false,
  [types.SHOW_SNACKBAR]: false
}

const mutations = {
  [types.SIDENAV_DRAWER](state, drawer) {
    state[types.SIDENAV_DRAWER] = drawer
  },
  [types.LOGIN_STATUS](state, status) {
    state[types.LOGIN_STATUS] = status
  },
  [types.CART_ITEMS](state, item) {
    state[types.SHOW_SNACKBAR] = true
    state[types.CART_ITEMS].push(item)
  },
  [types.SHOW_LOADING](state, show) {
    state[types.SHOW_LOADING] = show
  },
  [types.SHOW_SNACKBAR](state, snackbar) {
    state[types.SHOW_SNACKBAR] = snackbar
  }
}

const getters = {
  [types.CART_ITEMS_COUNT](state, getters) {
    return state[types.CART_ITEMS].length
  }
}

const actions = {}

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters,
  modules: {
    menu,
    doctorMember,
    edent,
    bitcoin,
    rioShop
  }
})
