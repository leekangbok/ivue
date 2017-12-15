import Vue from 'vue'
import Vuex from 'vuex'
import * as actions from './actions'
import * as getters from './getters'
import menu from './modules/menu'
import doctorMember from './modules/doctor/member'

Vue.use(Vuex)

export default new Vuex.Store({
  actions,
  getters,
  modules: {
    menu,
    doctorMember
  }
})
