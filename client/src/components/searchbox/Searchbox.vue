<template>
  <v-card-title>
    <v-text-field :max="max"
      autofocus
      append-icon="delete"
      single-line
      hide-details
      :value="value"
      :label="label"
      @input="n => $emit('input', n)"
      :append-icon-cb="onClose"
      @keyup.enter="() => $emit(targetEvent, 'enter')"
      :color="color"
      v-if="hiddenActiveSlot || show">
    </v-text-field>
    <iu-button text="search"
      icon
      iconOnly
      :color="color"
      flat
      @onEvent="show = !show"
      v-if="!hiddenActiveSlot && !show"></iu-button>
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
    },
    color: {
      type: String,
      default: 'primary'
    },
    hiddenActiveSlot: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      show: false
    }
  },
  methods: {
    onClose() {
      this.show = !this.show
      this.$emit(this.targetEvent, 'close')
    }
  },
  created() {}
}
</script>