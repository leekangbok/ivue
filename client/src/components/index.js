import Test from './test'
import Tabs from './tabs'
import { Box1xcol2 } from './container'
import SubHeader from './sub-header'
import Button from './button'
import Form from './form'
import Toolbar from './toolbar'
import Datatable from './data-table'
import Searchbox from './searchbox'

const components = {
  Test,
  Tabs,
  Box1xcol2,
  SubHeader,
  Button,
  Form,
  Toolbar,
  Datatable,
  Searchbox
}

export function iuComponentsInstall(Vue) {
  Object.keys(components).forEach(key => {
    Vue.component(`Iu${key}`, components[key])
  })
}
