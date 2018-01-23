import types from '../../mutation-types'
import api from '../../api'

const state = {
  productItems: []
}

const mutations = {
  setProductItems(state, data) {
    console.log(data)
    state.productItems = data.map(item => {
      return item
    })
  }
}

const getters = {
  [types.GET_RIOSHOP_PRODUCT_ITEMS](state, getters) {
    return state.productItems
  }
}

const actions = {
  [types.GET_RIOSHOP_PRODUCT_ITEMS]({ commit }, { query = '' } = {}) {
    commit(types.SHOW_LOADING, true)
    return api.request(
      'get',
      '/api/rio/shop/items',
      {
        params: { product: query }
      },
      response => {
        commit('setProductItems', response.data)
        commit(types.SHOW_LOADING, false)
      },
      error => {
        console.log(error)
        commit(types.SHOW_LOADING, false)
      }
    )
  }
}

export default {
  state,
  mutations,
  getters,
  actions
}
