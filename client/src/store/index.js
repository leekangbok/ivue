import Vue from 'vue'
import Vuex from 'vuex'
import menu from './modules/menu'
import doctorMember from './modules/doctor/member'
import edent from './modules/edent'
import bitcoin from './modules/bitcoin'
import types from './mutation-types'

Vue.use(Vuex)

const state = {
  [types.SIDENAV_DRAWER]: null,
  [types.LOGIN_STATUS]: false,
  [types.CART_ITEMS]: []
}

const mutations = {
  [types.SIDENAV_DRAWER](state, drawer) {
    state[types.SIDENAV_DRAWER] = drawer
  },
  [types.LOGIN_STATUS](state, status) {
    state[types.LOGIN_STATUS] = status
  },
  [types.CART_ITEMS](state, item) {
    state[types.CART_ITEMS].push(item)
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
    bitcoin
  }
})
