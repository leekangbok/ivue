<template>
  <v-app id="app-shop">
    <v-container fluid
      grid-list-sm
      text-xs-center>
      <v-layout row
        wrap
        justify-center>
        <v-flex xs12>
          <v-card flat>
          <v-layout row wrap justify-center>
            <v-flex sm8>
              <ShopTop></ShopTop>
            </v-flex>
          </v-layout>
          </v-card>
        </v-flex>
        <v-flex xs12>
          <v-card flat>
          <v-layout row wrap justify-center>
            <v-flex sm8>
          <ShopCenter></ShopCenter>
         </v-flex>
          </v-layout>
          </v-card>
        </v-flex>
        <v-flex xs12>
          <v-card flat>
          <v-layout row wrap justify-center>
            <v-flex sm8>
          <ShopBottom></ShopBottom>
        </v-flex>
          </v-layout>
          </v-card>
        </v-flex>
        <v-flex sm8>
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
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
