import Test from './test'

const components = {
  Test
}

export function iuComponentsInstall(Vue) {
  Object.keys(components).forEach(key => {
    Vue.component(`Iu${key}`, components[key])
  })
}
