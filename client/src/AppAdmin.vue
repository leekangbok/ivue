<template>
  <v-app id="inspire">
    <SideNav :items="menus"
      v-model="drawer"></SideNav>
    <TopNav app
      fixed
      flat
      dark
      color="blue-grey darken-4"
      @onSearch="onSearch"
      title="Google Contacts"
      :tabsItem="[{title: 'PB 상품'}, {title: '이벤트 특가'}, {title: '기구/샤프닝'}, {title: '게시판'}]">
      <div class="d-flex align-center"
        style="margin-left: auto">
        <MoreApps></MoreApps>
        <Notifications></Notifications>
        <Accounts></Accounts>
      </div>
    </TopNav>
    <v-content>
      <v-container>
        <transition name="route-fade"
          mode="out-in"
          appear>
          <router-view></router-view>
        </transition>
      </v-container>
    </v-content>
    <BottomNav></BottomNav>
  </v-app>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
import types from './store/mutation-types'
import SideNav from './components/SideNav'
import TopNav from './components/TopNav'
import BottomNav from './components/BottomNav'
import MoreApps from './components/MoreApps'
import Notifications from './components/Notifications'
import Accounts from './components/Accounts'

export default {
  components: {
    SideNav,
    TopNav,
    BottomNav,
    MoreApps,
    Notifications,
    Accounts
  },
  computed: {
    ...mapGetters({
      menus: types.GET_SIDEBAR_MENU
    }),
    drawer: {
      get() {
        return this.$store.state[types.SIDENAV_DRAWER]
      },
      set(value) {
        this.$store.commit(types.SIDENAV_DRAWER, value)
      }
    }
  },
  data() {
    return {}
  },
  methods: {
    onSearch(search) {
      console.log(search)
    }
  }
}
</script>

<style>
/* .content {
  background-color: white;
} */
.route-fade-enter-active,
.route-fade-leave-active {
  transition: opacity 0.5s;
}

.route-fade-enter,
.route-fade-leave-active {
  opacity: 0;
}

#inspire {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  /* margin: 60px 60px; */
}
</style>