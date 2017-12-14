<template>
  <div>
    <v-parallax :src="backImg"
      :height="backHeight">
      <v-layout column
        align-center
        justify-center
        class="white--text">
        <img :src="innerImg"
          :height="innerHeight"
          v-if="innerImg">
        <h1 class="white--text mb-2 display-1 text-xs-center">믿고 신뢰하는 리오치과</h1>
        <div class="subheading mb-3 text-xs-center">친절하고 정직한, 환자가 신뢰하는 치과</div>
      </v-layout>
    </v-parallax>

    <v-container>
      <v-carousel hide-controls
        delimiter-icon="stop">
        <v-carousel-item v-for="(item,i) in items"
          v-bind:src="item.src"
          :key="i"></v-carousel-item>
      </v-carousel>
    </v-container>
  </div>
</template>

<script>
export default {
  props: {
    backImg: String,
    backHeight: Number,
    innerImg: {
      type: String,
      default: null
    },
    innerHeight: Number
  },
  data() {
    return {
      items: [
        {
          src: 'src/assets/a.jpg'
        },
        {
          src: 'src/assets/a.png'
        },
        {
          src: 'src/assets/images1.jpeg'
        }
      ]
    }
  },
  methods: {
    onClick() {
      console.log('click')
    }
  }
}
</script>