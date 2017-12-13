import Vue from 'vue'
import VueRouter from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import store from '@/store'
import types from '@/store/mutation-types'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld
  },
  ...store.getters[types.GET_ROUTES]
]

export default new VueRouter({
  routes
})
