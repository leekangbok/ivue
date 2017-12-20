<template>
  <v-tabs :grow="expand"
    @input="change">
    <v-tabs-bar>
      <v-tabs-slider :color="slider.color"
        v-if="slider"></v-tabs-slider>
      <v-tabs-item :active-class="activeClass"
        :class="textClass"
        ripple
        v-for="(item, i) in items"
        :key="i"
        :href="`${id}` + i">
        {{ item.text }}
      </v-tabs-item>
    </v-tabs-bar>
  </v-tabs>
</template>

<script>
export default {
  name: 'IuTabs',
  props: {
    targetEvent: {
      type: String,
      default: 'onEvent'
    },
    id: {
      type: String,
      default: '#tab-'
    },
    items: {
      type: Array,
      default() {
        return []
      }
    },
    expand: {
      type: Boolean,
      default: true
    },
    activeClass: {
      type: String,
      default: null
    },
    textClass: {
      type: Object,
      default() {
        return {
          'primary--text': true
        }
      }
    },
    slider: {
      type: Object,
      default: null
    }
  },
  methods: {
    change(id) {
      this.$emit(this.targetEvent, this.items[parseInt(id.split('-')[1])], id)
    }
  }
}
</script>

<style>

.tabs__li {
  font-weight: bold;
}

</style>
