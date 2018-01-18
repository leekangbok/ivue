import Vue from 'vue'
import Vuex from 'vuex'
import * as actions from './actions'
import * as getters from './getters'
import menu from './modules/menu'
import doctorMember from './modules/doctor/member'
import edent from './modules/edent'
import bitcoin from './modules/bitcoin'
import types from './mutation-types'

Vue.use(Vuex)

const state = {
  [types.SIDENAV_DRAWER]: null
}

const mutations = {
  [types.SIDENAV_DRAWER](state, drawer) {
    state[types.SIDENAV_DRAWER] = drawer
  }
}

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
