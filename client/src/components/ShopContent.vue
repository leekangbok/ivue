<template>
  <v-container grid-list-lg>
    <v-layout row
      wrap
      justify-left>
      <v-flex v-bind="{ [`sm${item.flex}`]: true, 'xs12': true }"
        v-for="(item, index) in items"
        :key="index">
        <component :is="item.component"
          v-if="item.component"></component>
        <ShopItem :imgSrc="item.src"
          :title="item.title"
          v-else></ShopItem>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'
import types from '@/store/mutation-types'
import ShopContentNav from './ShopContentNav'
import ShopItem from './ShopItem'

export default {
  data() {
    return {
    }
  },
  components: {
    ShopContentNav,
    ShopItem
  },
  computed: {
    ...mapGetters({
      productItems: types.GET_RIOSHOP_PRODUCT_ITEMS
    }),
    items() {
      let items = this.productItems.slice()
      items.unshift({
        component: ShopContentNav,
        flex: 3
      })
      return items
    }
  }
}
</script>
