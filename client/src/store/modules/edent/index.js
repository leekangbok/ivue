import Types from '@/store/mutation-types'
import api from '@/store/api'
import types from '../../mutation-types'

const state = {
  items: [{ 'img': '/data/product/img_s1_30515', 'name': 'haram' }]
}

const mutations = {
  setItems(state, data) {
    console.log(data)
    state.items = data.map(item => {
      return item
    })
  }
}

const getters = {
  [types.GET_EDENT_HEADERS](state, getters) {
    return [{ text: '이미지', value: 'img', align: 'left' },
      { text: '상품명', value: 'name' },
      { text: '가격', value: 'price' }
    ]
  },
  [types.GET_EDENT_ITEMS](state, getters) {
    return state.items
  }
}

const actions = {
  [Types.GET_EDENT_ITEMS]({ commit }, { query = '' } = {}) {
    return api.request('get', '/project/search', {
        params: { product: query }
      },
      (response) => commit('setItems', response.data),
      (error) => console.log(error))
  }
}

export default {
  state,
  mutations,
  getters,
  actions
}
