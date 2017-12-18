<template>
  <v-card flat>
    <v-card-actions>
      <span class="primary--text">{{ text }}</span>
      <iu-button :text="icon"
        icon
        iconOnly
        @onEvent="show = !show"></iu-button>
    </v-card-actions>
    <v-slide-y-transition>
      <v-card-actions v-show="show">
        <slot>
        </slot>
      </v-card-actions>
    </v-slide-y-transition>
  </v-card>
</template>

<script>
export default {
  props: ['text'],
  data() {
    return {
      show: false
    }
  },
  computed: {
    icon() {
      return this.show ? 'keyboard_arrow_down' : 'keyboard_arrow_up'
    }
  }
}
</script>
