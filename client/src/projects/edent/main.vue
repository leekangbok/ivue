<template>
  <v-container v-bind="{ [`grid-list-${size}`]: true }">
    <v-layout justify-center>
      <v-flex xs12
        sm6>
        <iu-searchbox2 v-model="search"
          @onEvent="onSearch"
          autofocus
          text="상품명을 입력해주세요..."></iu-searchbox2>
      </v-flex>
    </v-layout>
    <v-layout justify-center
      row
      wrap>
      <v-flex v-bind="{ [`sm${card.flex}`]: true, 'xs12': true }"
        v-for="card in cards"
        :key="card.title">
        <v-card>
          <v-card-media :src="card.src"
            height="200px">
            <v-container fill-height
              fluid>
              <v-layout fill-height>
                <v-flex xs12
                  align-end
                  flexbox>
                  <span class="headline white--text"
                    v-text="card.title"></span>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card-media>
          <v-card-actions class="white">
            <v-spacer></v-spacer>
            <v-tooltip top
              color="green">
              <iu-button slot="activator"
                flat
                iconOnly
                icon="shopping_cart"
                color="green darken-2"></iu-button>
              <span>구매하기</span>
            </v-tooltip>
            <v-tooltip top
              color="green">
              <iu-button slot="activator"
                flat
                iconOnly
                icon="bookmark"></iu-button>
              <span>북마크</span>
            </v-tooltip>
            <v-tooltip top
              color="green">
              <iu-button slot="activator"
                flat
                iconOnly
                icon="description"></iu-button>
              <span>상세보기</span>
            </v-tooltip>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      size: 'lg',
      search: '',
      cards: [
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
  methods: {
    onSearch(event) {}
  }
}
</script>