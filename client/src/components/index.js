import axios from 'axios'
import Test from './test'
import Tabs from './tabs'
import { Box1xcol2 } from './container'
import SubHeader from './sub-header'
import Button from './button'
import Form from './form'
import Toolbar from './toolbar'
import Datatable from './data-table'
import Searchbox from './searchbox'
import Parallax from './parallax'
import C3 from './c3'
import Searchbox2 from './searchbox2'
import ToolbarNav from './toolbar-nav'

const components = {
  Test,
  Tabs,
  Box1xcol2,
  SubHeader,
  Button,
  Form,
  Toolbar,
  Datatable,
  Searchbox,
  Parallax,
  C3,
  Searchbox2,
  ToolbarNav
}

function componentsInstall(Vue) {
  Object.keys(components).forEach(key => {
    Vue.component(`Iu${key}`, components[key])
  })
}

export default {
  install(Vue, options) {
    componentsInstall(Vue)

    Vue.prototype.$http = axios
  }
}
