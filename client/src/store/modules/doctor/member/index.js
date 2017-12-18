import Types from '@/store/mutation-types'
import api from '@/store/api'

const state = {}

const mutations = {}

const getters = {}

const actions = {
  [Types.GET_DOCTOR_MEMBERS]({ commit }) {
    return api.request('get', '/api/doctor/member')
  }
}

export default {
  state,
  mutations,
  getters,
  actions
}
