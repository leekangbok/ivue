<template>
  <v-tabs fixed>
    <v-toolbar v-bind="$attrs" color="transparent">
      <v-toolbar-title class="ml-3 pl-3 mr-3 pl-3">
        <v-toolbar-side-icon @click.stop="drawer = !drawer" v-if="nav"></v-toolbar-side-icon>
        <slot name="title">
          <span :class="{'hidden-xs-only': hiddenTitle}"
          v-if="title.length">{{ title }}</span>
        </slot>
      </v-toolbar-title>
      
      <v-text-field prepend-icon="search"
        :prepend-icon-cb="() => $emit('onSearch', search)"
        @keyup.enter="$emit('onSearch', search)"
        v-model.trim="search"
        solo
        :append-icon="search ? 'clear' : ''"
        :append-icon-cb="() => search = ''"
        light
        style="max-width: 500px; min-width: 128px" v-if="searchBox"></v-text-field>


      <slot></slot>

      <v-tabs-bar color="transparent"
        dark
        slot="extension"
        v-if="tabsItem">
        <v-tabs-slider id="topnav-tabs-slider"
          color="white"></v-tabs-slider>
        <v-tabs-item ripple
          v-for="(item, i) in tabsItem"
          :key="i"
          :href="'#tab-' + item.title">
          {{ item.title }}
        </v-tabs-item>
      </v-tabs-bar>
    </v-toolbar>
  </v-tabs>
</template>

<script>
import types from '@/store/mutation-types'

export default {
  props: {
    hiddenTitle: Boolean,
    searchBox: Boolean,
    nav: Boolean,
    tabsItem: {
      type: Array,
      default: null
    },
    title: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      searchMode: false,
      search: ''
    }
  },
  computed: {
    drawer: {
      get() {
        return this.$store.state[types.SIDENAV_DRAWER]
      },
      set(value) {
        this.$store.commit(types.SIDENAV_DRAWER, value)
      }
    }
  }
}
</script>
