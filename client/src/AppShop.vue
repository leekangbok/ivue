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
                sm6
                md8>
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
                sm6
                md8>
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
              sm6
              md8>
              <ShopBottom></ShopBottom>
            </v-flex>
          </v-layout>
        </v-card>
      </v-flex>
      <v-flex xs12
        sm6
        md8>
        <ShopContent></ShopContent>
      </v-flex>
    </v-layout>
            <Loading
            :show="show"
            :label="label"
            >
        </Loading>
      </v-container>
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
