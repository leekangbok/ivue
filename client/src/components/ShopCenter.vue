<template>
  <div>
    <iu-toolbar-nav searchBox
      hiddenTitle
      @onSearch="onSearch">
      <v-icon large
        slot="title">home</v-icon>
      <!-- <span class="hidden-xs-only">Dshop</span> -->
      <!-- <v-avatar size="40px"
          slot="title">
          <img src="src/assets/search.jpg">
    </v-avatar> -->
      <div class="d-flex align-center"
        style="margin-left: auto">
        <Notifications @click.native.stop="dialog = true"></Notifications>
        <MyShop></MyShop>
      </div>
    </iu-toolbar-nav>
    <v-dialog v-model="dialog"
      max-width="390">
      <v-card>
        <v-card-title class="headline">구매상품 리스트</v-card-title>
        <v-card-text>지금까지 담겨진 상품들 보여주고 결재하기.</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1"
            flat="flat"
            @click.native="dialog = false">확인</v-btn>
          <v-btn color="green darken-1"
            flat="flat"
            @click.native="dialog = false">결제</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import Notifications from './Notifications'
import MyShop from './MyShop'
import types from '@/store/mutation-types'

export default {
  data() {
    return {
      search: '',
      dialog: false
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
