<template>
  <v-app id="app-shop">
    <v-container fluid>
      <v-layout row
        wrap
        justify-center>
        <v-flex xs12>
          <iu-panel flat
            dark
            :bgImg="topBgImg">
            <v-layout row
              wrap
              justify-center>
              <v-flex v-bind="{ [`xs${xsflex}`]: true, [`sm${smflex}`]: true, [`md${mdflex}`]: true, [`lg${lgflex}`]: true, [`xl${xlflex}`]: true }">
                <ShopTop></ShopTop>
              </v-flex>
            </v-layout>
          </iu-panel>
        </v-flex>
        <v-flex xs12>
          <v-divider class="cyan darken-1"></v-divider>
        </v-flex>
        <v-flex xs12>
          <iu-panel flat
            dark
            :bgImg="topBgImg">
            <v-layout row
              wrap
              justify-center>
              <v-flex v-bind="{ [`xs${xsflex}`]: true, [`sm${smflex}`]: true, [`md${mdflex}`]: true, [`lg${lgflex}`]: true, [`xl${xlflex}`]: true }">
                <ShopCenter></ShopCenter>
              </v-flex>
            </v-layout>
          </iu-panel>
        </v-flex>
        <v-flex xs12>
          <iu-panel flat>
            <v-layout row
              wrap
              justify-center>
              <v-flex v-bind="{ [`xs${xsflex}`]: true, [`sm${smflex}`]: true, [`md${mdflex}`]: true, [`lg${lgflex}`]: true, [`xl${xlflex}`]: true }">
                <ShopBottom></ShopBottom>
              </v-flex>
            </v-layout>
          </iu-panel>
        </v-flex>
        <v-flex v-bind="{ [`xs${xsflex}`]: true, [`sm${smflex}`]: true, [`md${mdflex}`]: true, [`lg${lgflex}`]: true, [`xl${xlflex}`]: true }">
          <ShopContent></ShopContent>
        </v-flex>
      </v-layout>
      <Loading :show="show"
        :label="label">
      </Loading>
    </v-container>
    <v-snackbar :timeout="3000"
      v-model="snackbar"
      color="green darken-2">
      {{ snackbarText }}
      <v-btn dark
        flat
        @click.native="snackbar = false">확인</v-btn>
    </v-snackbar>
  </v-app>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import Loading from 'vue-full-loading'
import types from '@/store/mutation-types'
import ShopTop from './components/ShopTop'
import ShopCenter from './components/ShopCenter'
import ShopBottom from './components/ShopBottom'
import ShopContent from './components/ShopContent'

export default {
  data() {
    return {
      xsflex: 12,
      smflex: 12,
      mdflex: 12,
      lgflex: 11,
      xlflex: 10,
      label: '로딩중.....',
      topBgImg: 'src/assets/bg2.svg'
    }
  },
  components: {
    ShopTop,
    ShopCenter,
    ShopBottom,
    ShopContent,
    Loading
  },
  computed: {
    snackbar: {
      get() {
        return this.showSnackbar
      },
      set(value) {
        this[types.SHOW_SNACKBAR](value)
      }
    },
    ...mapState({
      showSnackbar: types.SHOW_SNACKBAR,
      show: types.SHOW_LOADING,
      snackbarText: types.SNACKBAR_TEXT
    })
  },
  methods: {
    ...mapMutations([types.SHOW_SNACKBAR])
  },
  mounted() {}
}
</script>

<style>
.route-fade-enter-active,
.route-fade-leave-active {
  transition: opacity 0.5s;
}

.route-fade-enter,
.route-fade-leave-active {
  opacity: 0;
}

#app-shop {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50 !important;
  font-size: 12px !important;
  /* font-weight: bold; */
}

.list__tile__title {
  font-size: 12px !important;
  /* font-weight: bold; */
}

.toolbar__title {
  font-size: 16px !important;
  /* font-weight: bold; */
}

.btn--small {
  font-size: 12px !important;
  /* height: 24px !important; */
}

.btn__content {
  margin-right: 0px !important;
  margin-left: 0px !important;
  padding-right: 0px !important;
  padding-left: 0px !important;
}

.btn {
  min-width: 0px !important;
  padding-left: 5px !important;
  padding-right: 5px !important;
}

a.tabs__item.tabs__item--active {
  color: darkcyan !important;
  font-size: 13px !important;
  font-weight: bold !important;
}

.tabs__item {
  font-weight: bold !important;
}

a.tabs__item:hover {
  color: darkcyan !important;
}
</style>
