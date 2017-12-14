import Test from './test'
import Tabs from './tabs'
import { Box1xcol2 } from './container'
import SubHeader from './sub-header'
import Button from './button'
import Form from './form'

const components = {
  Test,
  Tabs,
  Box1xcol2,
  SubHeader,
  Button,
  Form
}

export function iuComponentsInstall(Vue) {
  Object.keys(components).forEach(key => {
    Vue.component(`Iu${key}`, components[key])
  })
}
