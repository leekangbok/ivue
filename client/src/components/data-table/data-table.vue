<template>
  <v-container>
    <slot></slot>
    <v-data-table :headers="headers"
      :items="items"
      :search="search"
      :pagination="pagination"
      @update:pagination="n => $emit('update:pagination', n)"
      :total-items="serverSide ? totalItems : null"
      :loading="serverSide ? loading : false"
      :value="value"
      @input="n => $emit('input', n)"
      :item-key="itemKey"
      :select-all="selectable ? true : false"
      class="elevation-0"
      :rows-per-page-items="[5, 15, 25, 45, 85, { text: 'All', value: -1 }]"
      rows-per-page-text=""
      no-results-text=""
      no-data-text="">
      <template slot="headerCell"
        slot-scope="props">
        <v-tooltip bottom>
          <span slot="activator">
            {{props.header.tooltip || props.header.text || ''}}
          </span>
          <span>
            {{props.header.text || ''}}
          </span>
        </v-tooltip>
      </template>
      <template slot="items"
        slot-scope="props">
        <tr @click="$emit('onRowClick', props.item)">
          <td @click="e => e.stopPropagation()"
            v-if="selectable">
            <v-checkbox primary
              hide-details
              v-model="props.selected"></v-checkbox>
          </td>
          <template v-for="(header, index) of headers">
            <td :class="{ 'text-xs-right': !!index }"
              v-if="header.render"
              :key="index">
              <Expand :row="props.item"
                :column="props.item[header.value]"
                :render="header.render">
              </Expand>
            </td>
            <td :class="{ 'text-xs-right': !!index }"
              v-else
              :key="index">{{props.item[header.value]}}</td>
          </template>
        </tr>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import Expand from './expand'

export default {
  props: {
    serverSide: {
      type: Boolean,
      default: true
    },
    selectable: {
      type: Boolean,
      default: true
    },
    headers: Array,
    items: Array,
    totalItems: {
      type: Number,
      default: 0
    },
    loading: {
      type: Boolean,
      default: true
    },
    pagination: {
      type: Object,
      default() {
        return {}
      }
    },
    value: {
      type: Array,
      default() {
        return []
      }
    },
    itemKey: {
      type: String,
      default: ''
    },
    search: {
      type: String,
      default: ''
    }
  },
  data() {
    return {}
  },
  watch: {},
  methods: {},
  components: {
    Expand
  },
  created() {}
}
</script>