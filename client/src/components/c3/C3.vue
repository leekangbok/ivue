<template>
  <vue-c3 :handler="handler"></vue-c3>
</template>


<script>
import Vue from 'vue'
import VueC3 from 'vue-c3'

export default {
  components: {
    VueC3
  },
  props: ['options'],
  data() {
    return {
      handler: new Vue()
    }
  },
  mounted() {
    this.handler.$emit('init', this.options)
  },
  watch: {
    'options.data': {
      handler(data) {
        this.handler.$emit('dispatch', chart => chart.load(data))
      }
    }
  }
}
</script>