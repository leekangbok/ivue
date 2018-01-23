<template>
  <v-tabs fixed>
    <v-toolbar v-bind="$attrs">
      <v-toolbar-title :style="$vuetify.breakpoint.smAndUp ? 'width: 300px; min-width: 250px' : 'min-width: 172px'"
        class="ml-0 pl-3"
        v-if="!searchMode">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <span class="hidden-xs-only"
          v-if="title.length">{{ title }}</span>
      </v-toolbar-title>
      <template v-else>
        <v-btn @click="searchMode=!searchMode"
          icon>
          <v-icon>arrow_back</v-icon>
        </v-btn>
        <v-text-field prepend-icon="search"
          :prepend-icon-cb="() => $emit('onSearch', search)"
          @keyup.enter="$emit('onSearch', search)"
          v-model.trim="search"
          solo
          :append-icon="search ? 'clear' : ''"
          :append-icon-cb="() => search = ''"
          hide-details
          light
          single-line
          style="min-width: 130px"></v-text-field>
      </template>
      <div class="d-flex align-center"
        style="margin-left: auto">
        <v-btn @click="searchMode=!searchMode"
          icon
          v-if="!searchMode">
          <v-icon>search</v-icon>
        </v-btn>
        <slot></slot>
      </div>
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

<style>
#topnav-tabs-slider {
  height: 4px;
}
</style>
