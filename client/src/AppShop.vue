<template>
  <v-app id="app-shop">
    <v-container fluid
      grid-list-sm
      text-xs-center
      app>
      <v-layout row
        wrap
        justify-center>
        <v-flex xs12>
          <v-card flat
            color="primary"
            dark>
            <v-layout row
              wrap
              justify-center>
              <v-flex xs12
                md12
                sm8>
                <ShopTop></ShopTop>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
        <v-flex xs12>
          <v-card flat
            color="primary"
            dark>
            <v-layout row
              wrap
              justify-center>
              <v-flex xs12
                md12
                sm8>
                <ShopCenter></ShopCenter>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
        <v-flex xs12>
          <v-card flat>
            <v-layout row
              wrap
              justify-center>
              <v-flex xs12
                md12
                sm8>
                <ShopBottom></ShopBottom>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
        <v-flex xs12
          md12
          sm8>
          <ShopContent></ShopContent>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
import ShopTop from './components/ShopTop'
import ShopCenter from './components/ShopCenter'
import ShopBottom from './components/ShopBottom'
import ShopContent from './components/ShopContent'

export default {
  components: {
    ShopTop,
    ShopCenter,
    ShopBottom,
    ShopContent
  }
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
  font-weight: bold;
}

.list__tile__title {
  font-size: 12px !important;
  font-weight: bold;
}

.toolbar__title {
  font-size: 16px !important;
  font-weight: bold;
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
</style>
