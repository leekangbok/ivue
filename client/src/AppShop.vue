<template>
  <v-app id="app-shop">
    <v-container fluid>
      <v-layout row
        wrap
        justify-center>
        <v-flex xs12>
          <v-card flat
            dark>
            <v-card-media :src="topBgImg">
              <v-layout row
                wrap
                justify-center>
                <v-flex xs12
                  md10>
                  <ShopTop></ShopTop>
                </v-flex>
              </v-layout>
            </v-card-media>
          </v-card>
        </v-flex>
        <v-flex xs12>
          <v-card flat
            dark>
            <v-card-media :src="topBgImg">
              <v-layout row
                wrap
                justify-center>
                <v-flex xs12
                  md10>
                  <ShopCenter></ShopCenter>
                </v-flex>
              </v-layout>
            </v-card-media>
          </v-card>
        </v-flex>
        <v-flex xs12>
          <v-card flat>
            <v-layout row
              wrap
              justify-center>
              <v-flex xs12
                md10>
                <ShopBottom></ShopBottom>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
        <v-flex xs12
          md10>
          <ShopContent></ShopContent>
        </v-flex>
      </v-layout>
      <Loading :show="show"
        :label="label">
      </Loading>
    </v-container>
    <v-snackbar :timeout="3000"
      v-model="snackbar"
      color="cyan darken-2">
      {{ snackbarText }}
      <v-btn dark
        flat
        @click.native="snackbar = false">확인</v-btn>
    </v-snackbar>
  </v-app>
</template>

<script>
import Loading from 'vue-full-loading'
import types from '@/store/mutation-types'
import ShopTop from './components/ShopTop'
import ShopCenter from './components/ShopCenter'
import ShopBottom from './components/ShopBottom'
import ShopContent from './components/ShopContent'

export default {
  data() {
    return {
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
    show() {
      return this.$store.state[types.SHOW_LOADING]
    },
    snackbar: {
      get() {
        return this.$store.state[types.SHOW_SNACKBAR]
      },
      set(value) {
        this.$store.commit(types.SHOW_SNACKBAR, value)
      }
    },
    snackbarText() {
      return '장바구니에 땡땡땡을 추가했습니다.'
    }
  }
}
</script>

<style
>
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

.tabs__item {
  font-weight: bold !important;
}

.tabs__item--active {
  font-size: 13px !important;
  font-weight: bold !important;
}
</style>
