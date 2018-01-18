<template>
  <v-card-actions>
    <v-spacer v-for="i of spacer"
      :key="i"></v-spacer>
    <slot></slot>
  </v-card-actions>
</template>

<script>
export default {
  props: {
    spacer: {
      type: Number,
      default: 1
    }
  }
}
</script>
