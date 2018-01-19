<template>
<v-container grid-list-lg>
    <v-layout row
      wrap justify-center>
      <v-flex v-bind="{ [`sm${item.flex}`]: true, 'xs12': true }"
        v-for="(item, index) in items"
        :key="index">
        <component :is="item.component" v-if="item.component"></component>
        <ShopItem :imgSrc="item.src" :title="item.title" v-else></ShopItem>
      </v-flex>
    </v-layout>
</v-container>
</template>

<script>
import ShopContentNav from './ShopContentNav'
import ShopItem from './ShopItem'

export default {
  data() {
    return {
      items: [
        {
          component: ShopContentNav,
          flex: 3
        },
        {
          title: 'Pre-fab homes',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Favorite road trips',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Best airlines',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Pre-fab homes',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Favorite road trips',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Best airlines',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Pre-fab homes',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Favorite road trips',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Best airlines',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Pre-fab homes',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Favorite road trips',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Best airlines',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Pre-fab homes',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Favorite road trips',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Best airlines',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Pre-fab homes',
          src: 'http://www.edent.co.kr/data/product/img_m1_14042',
          flex: 3
        },
        {
          title: 'Favorite road trips',
          src: '/static/doc-images/cards/road.jpg',
          flex: 3
        },
        {
          title: 'Best airlines',
          src: '/static/doc-images/cards/plane.jpg',
          flex: 3
        },
        {
          title: 'Pre-fab homes',
          src: '/static/doc-images/cards/house.jpg',
          flex: 3
        },
        {
          title: 'Favorite road trips',
          src: '/static/doc-images/cards/road.jpg',
          flex: 3
        },
        {
          title: 'Best airlines',
          src: '/static/doc-images/cards/plane.jpg',
          flex: 3
        },
        {
          title: 'Pre-fab homes',
          src: '/static/doc-images/cards/house.jpg',
          flex: 3
        },
        {
          title: 'Favorite road trips',
          src: '/static/doc-images/cards/road.jpg',
          flex: 3
        },
        {
          title: 'Best airlines',
          src: '/static/doc-images/cards/plane.jpg',
          flex: 3
        },
        {
          title: 'Pre-fab homes',
          src: '/static/doc-images/cards/house.jpg',
          flex: 3
        },
        {
          title: 'Favorite road trips',
          src: '/static/doc-images/cards/road.jpg',
          flex: 3
        },
        {
          title: 'Best airlines',
          src: '/static/doc-images/cards/plane.jpg',
          flex: 3
        }
      ]
    }
  },
  components: {
    ShopContentNav,
    ShopItem
  }
}
</script>
