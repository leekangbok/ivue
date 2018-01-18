<template>
    <v-tabs fixed color="transparent">
    <v-tabs-bar>
      <v-tabs-slider></v-tabs-slider>
      <v-tabs-item
        v-for="i in items"
        :key="i"
        :href="'#tab-' + i"
      >
        {{ i }}
      </v-tabs-item>
    </v-tabs-bar>
  </v-tabs>
</template>

<script>
export default {
  data() {
    return {
      items: ['PB상품', '특가/세일', '기구 샤프닝', '소모품', '게시판'],
      text:
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
    }
  }
}
</script>
