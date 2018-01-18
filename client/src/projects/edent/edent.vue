<template>
  <v-container>
    <v-layout justify-center>
      <v-flex xs12
        sm6>
        <iu-searchbox @onEvent="onSearch"
          v-model="search"
          color="orange"
          hiddenActiveSlot>
        </iu-searchbox>
      </v-flex>
    </v-layout>
    <v-container>
      <v-layout justify-center>
        <v-flex xs12>
          <iu-datatable :headers="viewHeaders"
            :items="items"
            :serverSide="false"
            :selectable="false"
            :search="itemSearch">
            <iu-toolbar>
              <iu-searchbox v-model="itemSearch"
                @onEvent="itemSearch=''"></iu-searchbox>
            </iu-toolbar>
          </iu-datatable>
        </v-flex>
      </v-layout>
    </v-container>
  </v-container>
</template>

<script>
import Types from '@/store/mutation-types'
import { mapActions, mapGetters } from 'vuex'

export default {
  data() {
    return {
      // headers: [
      //   {
      //     text: '이미지',
      //     value: 'image',
      //     align: 'left',
      //     render: (createElement, params) => {
      //       return createElement('img', {
      //         attrs: { src: ['http://www.edent.co.kr', params.column].join('') }
      //       })
      //     }
      //   },
      //   { text: '상품명', value: 'name' }
      // ],
      search: '',
      itemSearch: ''
    }
  },
  methods: {
    onSearch(event) {
      if (event === 'close') {
        this.search = ''
      } else if (event === 'enter' && this.search.length) {
        this.getEdentItems({ query: this.search }).then(response =>
          console.log('getEdentItems Complete.')
        )
      }
    },
    ...mapActions({
      getEdentItems: Types.GET_EDENT_ITEMS
    })
  },
  computed: {
    ...mapGetters({
      headers: Types.GET_EDENT_HEADERS,
      items: Types.GET_EDENT_ITEMS
    }),
    viewHeaders() {
      this.headers[0].render = (createElement, params) => {
        return createElement('img', {
          attrs: { src: ['http://www.edent.co.kr', params.column].join('') }
        })
      }
      this.headers[1].render = (createElement, params) => {
        return createElement(
          'a',
          {
            attrs: {
              href: ['http://www.edent.co.kr', params.row.href].join('')
            }
          },
          params.column
        )
      }
      return this.headers
    }
  }
}
</script>
