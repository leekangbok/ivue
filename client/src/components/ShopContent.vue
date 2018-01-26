<template>
    <v-layout row
      wrap
      justify-left align-center>
      <!-- <v-flex xs3>
        <ShopContentNav></ShopContentNav>
      </v-flex>
      <v-flex xs9>
      <v-layout row wrap justify-left> -->
      <v-flex v-bind="{ [`sm${item.flex}`]: true, 'xs12': true }"
        v-for="(item, index) in items"
        :key="index">
        <component :is="item.component"
          v-if="item.component" v-bind="item.attrs"></component>
        <ShopItem :imgSrc="item.src"
          :title="item.title" :height="height"
          v-else></ShopItem>
      </v-flex>
      <!-- </v-layout>
      </v-flex> -->
    </v-layout>
</template>

<script>
import { mapGetters } from 'vuex'
import types from '@/store/mutation-types'
import ShopContentNav from './ShopContentNav'
import ShopItem from './ShopItem'
import ShopSite from './ShopSite'

export default {
  data() {
    return {
      height: 300
    }
  },
  components: {
    ShopContentNav,
    ShopItem,
    ShopSite
  },
  computed: {
    ...mapGetters({
      productItems: types.GET_RIOSHOP_PRODUCT_ITEMS
    }),
    items() {
      return [
        { component: ShopContentNav, flex: 3, attrs: {} },
        { component: ShopSite, flex: 9 },
        ...this.productItems
      ]
    }
  }
}
</script>
