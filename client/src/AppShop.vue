<template>
  <v-app id="app-shop">
    <v-container fluid
      grid-list-sm
      text-xs-center>
      <v-layout row
        wrap
        justify-center>
        <v-flex xs12>
          <ShopTop></ShopTop>
        </v-flex>
        <v-flex xs12>
          <ShopCenter></ShopCenter>
        </v-flex>
        <v-flex xs12>
          <v-card dark
            color="primary">
            <v-card-text class="px-0">12</v-card-text>
          </v-card>
        </v-flex>
        <v-flex sm10>
          <v-card dark
            color="secondary">
            <v-card-text class="px-0">9</v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
import ShopTop from './components/ShopTop'
import ShopCenter from './components/ShopCenter'

export default {
  components: {
    ShopTop,
    ShopCenter
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