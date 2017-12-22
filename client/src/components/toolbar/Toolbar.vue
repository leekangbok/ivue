<template>
  <v-toolbar flat
    :color="color">
    <v-spacer v-for="i of spacer"
      :key="i"></v-spacer>
    <slot></slot>
  </v-toolbar>
</template>

<script>
export default {
  props: {
    spacer: {
      type: Number,
      default: 1
    },
    color: {
      type: String,
      default: 'white'
    }
  },
  data() {
    return {}
  }
}
</script>

<style>
.toolbar__content {
  padding-right: 25px;
}
</style>