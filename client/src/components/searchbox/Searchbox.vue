<template>
  <v-card-title>
    <v-text-field :max="max"
      autofocus
      append-icon="cancel"
      single-line
      hide-details
      :value="value"
      :label="label"
      @input="n => $emit('input', n)"
      :append-icon-cb="onCancel"
      @keyup.enter="() => $emit(targetEvent, 'enter')"
      loading
      light
      v-if="show">
      <v-progress-linear slot="progress"
        :value="progress"
        height="3"
        :color="color"></v-progress-linear>
    </v-text-field>
    <iu-button text="search"
      icon
      iconOnly
      color=""
      @onEvent="show = !show"
      v-if="!show"></iu-button>
  </v-card-title>
</template>                                                                                                                                                                                       
                                                                                                                                                                                                  
<script>
export default {
  props: {
    targetEvent: {
      type: String,
      default: 'onEvent'
    },
    value: {
      type: String,
      default: ''
    },
    max: {
      type: Number,
      default: 30
    },
    label: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      show: false
    }
  },
  computed: {
    progress() {
      return Math.min(100, this.value.length * 10)
    },
    color() {
      return ['primary'][Math.floor(this.progress / 40)]
    }
  },
  methods: {
    onCancel() {
      this.show = !this.show
      this.$emit(this.targetEvent, 'cancel')
    }
  }
}
</script>