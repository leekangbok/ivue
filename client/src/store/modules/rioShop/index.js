import types from '../../mutation-types'
import api from '../../api'

const state = {
  productItems: [],
  site: ['all']
}

const mutations = {
  setProductItems(state, data) {
    state.productItems = data.map(item => {
      return Object.assign(item, { flex: 3 })
    })
  },
  setSite(state, site = ['all']) {
    state.site = site
  }
}

const getters = {
  [types.GET_RIOSHOP_PRODUCT_ITEMS](state, getters) {
    return state.productItems.filter(({ site = 'all' }) => {
      if (
        state.site.findIndex(x => x === 'all') > 0 ||
        state.site.findIndex(x => x === site)
      ) {
        return true
      }
      return false
    })
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
        commit('setSite')
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
