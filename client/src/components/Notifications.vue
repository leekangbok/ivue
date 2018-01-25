<template>
  <v-btn icon
    small
    flat>
    <v-badge top
      color="green">
      <span slot="badge">{{ cartItemsCount }}</span>
      <v-icon>shopping_cart</v-icon>
    </v-badge>
  </v-btn>
</template>

<script>
import { mapGetters } from 'vuex'
import types from '@/store/mutation-types'

export default {
  computed: {
    ...mapGetters({
      cartItemsCount: types.CART_ITEMS_COUNT
    })
  }
}
</script>