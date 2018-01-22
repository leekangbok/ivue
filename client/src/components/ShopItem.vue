<template>
  <v-card>
    <v-card-media :src="imgSrc"
      height="200px">
      <v-container fill-height
        fluid>
        <v-layout fill-height>
          <v-flex xs12
            align-end
            flexbox>
            <span class="headline white--text"
              v-text="title"></span>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card-media>
    <v-card-actions class="white">
      <v-spacer></v-spacer>
      <v-tooltip top
        color="green">
        <v-btn @click="onCart(title)"
          icon
          slot="activator">
          <v-icon color="green darken-2">shopping_cart</v-icon>
        </v-btn>
        <span>구매하기</span>
      </v-tooltip>
      <v-tooltip top
        color="green">
        <v-btn icon
          slot="activator">
          <v-icon color="grey lighten-1">bookmark</v-icon>
        </v-btn>
        <span>북마크</span>
      </v-tooltip>
      <v-tooltip top
        color="green">
        <v-btn icon
          slot="activator">
          <v-icon color="grey lighten-1">description</v-icon>
        </v-btn>
        <span>상세보기</span>
      </v-tooltip>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapMutations } from 'vuex'
import types from '@/store/mutation-types'

export default {
  props: ['title', 'imgSrc'],
  methods: {
    ...mapMutations({
      onCart: types.CART_ITEMS
    })
  }
}
</script>
