import Types from '@/store/mutation-types'
import api from '@/store/api'
import types from '../../mutation-types'

const state = {
  ma: {
    data: {
      // x: 'x',
      columns: [
        // ['x', '2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04', '2013-01-05', '2013-01-06'],
        // ['ma5', 2, 4, 1, 5, 2, 1],
        // ['data2', 7, 2, 4, 6, 10, 1]
      ]
    },
    zoom: {
      enabled: true,
      rescale: true
    },
    subchart: {
      show: true
    },
    point: {
      r: 1.5
    },
    size: {
      height: 580
    }
    // axis: {
    //   x: {
    //     type: 'timeseries',
    //     tick: {
    //       format: '%Y-%m-%d'
    //     }
    //   }
    // }
  }
}

const mutations = {
  setMa(state, data) {
    // let ma5 = data.ma5.keys()
    let ma5 = ['ma5']
    Object.entries(data.ma5).forEach(([key, value]) => {
      ma5[parseInt(key) + 1] = value
    })
    let ma20 = ['ma20']
    Object.entries(data.ma20).forEach(([key, value]) => {
      ma20[parseInt(key) + 1] = value
    })
    let ma40 = ['ma40']
    Object.entries(data.ma40).forEach(([key, value]) => {
      ma40[parseInt(key) + 1] = value
    })
    let ma60 = ['ma60']
    Object.entries(data.ma60).forEach(([key, value]) => {
      ma60[parseInt(key) + 1] = value
    })
    let ma80 = ['ma80']
    Object.entries(data.ma80).forEach(([key, value]) => {
      ma80[parseInt(key) + 1] = value
    })
    let ma120 = ['ma120']
    Object.entries(data.ma120).forEach(([key, value]) => {
      ma120[parseInt(key) + 1] = value
    })
    let ma180 = ['ma180']
    Object.entries(data.ma180).forEach(([key, value]) => {
      ma180[parseInt(key) + 1] = value
    })
    console.log(ma5)
    console.log(ma20)
    console.log(ma40)
    console.log(ma60)
    console.log(ma80)

    state.ma.data = {
        columns: [
          ma5, ma20, ma40, ma60, ma80, ma120, ma180
        ]
      }
      // console.log(data)
      // state.ma = data.map(item => {
      //   return item
      // })
  }
}

const getters = {
  [types.GET_BITCOIN_RECENT_TRANSACTIONS](state, getters) {
    return state.ma
  }
}

const actions = {
  [Types.GET_BITCOIN_RECENT_TRANSACTIONS]({ commit }, { startDate = '', endDate = '', startTime = '', endTime = '', type = '' } = {}) {
    return api.request('get', '/api/coin/cryptoCurrencies', {
        params: { startDate, endDate, startTime, endTime, type }
      },
      (response) => commit('setMa', response.data),
      (error) => console.log(error))
  }
}

export default {
  state,
  mutations,
  getters,
  actions
}
