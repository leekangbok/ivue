<template>
  <div>
    <iu-toolbar-nav :searchBox="searchBox"
      @onSearch="onSearch">
      <v-icon large
        slot="title">list</v-icon>
      <iu-panel flat
        slot="link"
        color="transparent">
        <v-card-actions>
          <v-btn flat
            small
            class="caption">베스트100</v-btn>
          <v-btn flat
            small
            class="caption">PB몰</v-btn>
          <v-btn flat
            small
            class="caption">이벤트</v-btn>
          <v-btn flat
            small
            outline>
            <v-icon class="caption">list</v-icon>카테고리 더보기
          </v-btn>
        </v-card-actions>
      </iu-panel>
      <v-btn icon
        class="hidden-sm-and-up"
        @click.stop="searchBox=!searchBox">
        <v-icon>{{searchBox ? 'arrow_forward' : 'search'}}</v-icon>
      </v-btn>
      <Notifications @click.native.stop="dialog = true"></Notifications>
      <MyShop></MyShop>
    </iu-toolbar-nav>
    <v-dialog v-model="dialog"
      max-width="390">
      <v-card>
        <v-card-title class="headline">구매상품 리스트</v-card-title>
        <v-card-text>지금까지 담겨진 상품들 보여주고 결재하기.</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary"
            @click.native="dialog = false">확인</v-btn>
          <v-btn color="primary"
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
      searchBox: true,
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
  },
  watch: {
    '$vuetify.breakpoint': {
      handler: function(n) {
        console.log(n)
        if (n.smAndDown) {
          this.searchBox = false
        }
        if (n.smAndUp) {
          this.searchBox = true
        }
      },
      immediate: true
    }
  }
}
</script>
