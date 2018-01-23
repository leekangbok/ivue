<template>
  <iu-toolbar-nav searchBox hiddenTitle @onSearch="onSearch">
      <v-icon large slot="title">home</v-icon>
      <!-- <span class="hidden-xs-only">Dshop</span> -->
    <!-- <v-avatar size="40px"
          slot="title">
          <img src="src/assets/search.jpg">
    </v-avatar> -->
    <div class="d-flex align-center"
      style="margin-left: auto">
      <Notifications></Notifications>
      <MyShop></MyShop>
    </div>
  </iu-toolbar-nav>
</template>

<script>
import { mapActions } from 'vuex'
import Notifications from './Notifications'
import MyShop from './MyShop'
import types from '@/store/mutation-types'

export default {
  data() {
    return {
      search: ''
    }
  },
  components: {
    Notifications,
    MyShop
  },
  methods: {
    onSearch(text) {
      this[types.GET_RIOSHOP_PRODUCT_ITEMS]({ query: text }).then(response =>
        console.log(response)
      )
    },
    ...mapActions([types.GET_RIOSHOP_PRODUCT_ITEMS])
  }
}
</script>
