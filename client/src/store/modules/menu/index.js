import _ from 'lodash'
import types from '../../mutation-types'
import blog from './blog'
import dental from './dental'
import stock from './stock'
import customer from './customer'
import liveStream from './live-stream'
import home from './home'

function genRoutes(menu = [], routes = []) {
  for (let i = 0, l = menu.length; i < l; i++) {
    let item = menu[i]

    if (item.path) {
      routes.push(item)
    }
    if (!item.component) {
      genRoutes(item.children, routes)
    }
  }
  return routes
}

const state = {
  menus: [...blog, ...dental, ...stock, ...customer, ...liveStream, ...home]
}

const mutations = {}

const getters = {
  [types.GET_SIDEBAR_MENU](state, getters) {
    return _.sortBy(_.filter(state.menus, n => n.pri), [
      function(o) {
        return o.pri
      }
    ])
  },
  [types.GET_ROUTES](state, getters) {
    return genRoutes(state.menus)
  }
}

export default {
  state,
  mutations,
  getters
}
