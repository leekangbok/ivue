<template>
  <v-parallax :src="backImg"
    :height="backImgHeight">
    <v-layout column
      align-center
      justify-center
      :class="classes">
      <img :src="innerImg"
        :height="innerImgHeight"
        v-if="innerImg">
      <h1 class="white--text mb-2 display-1 text-xs-center"
        :class="classes"
        v-if="centerText">{{ centerText }}</h1>
      <div class="subheading mb-3 text-xs-center"
        v-if="subText">{{ subText }}</div>
    </v-layout>
  </v-parallax>
</template>

<script>
export default {
  props: [
    'backImg',
    'backImgHeight',
    'innerImg',
    'innerImgHeight',
    'centerText',
    'subText',
    'classes'
  ],
  data() {
    return {}
  }
}
</script>
