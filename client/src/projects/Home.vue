<template>
  <!-- <v-app> -->
  <v-container fluid>
    <v-layout justify-center>
      <v-flex xs12
        sm6>
        <iu-datatable :headers="headers"
          :items="records"
          :serverSide="false"
          :selectable="false"
          :search="search">
          <iu-toolbar>
            <iu-searchbox v-model="search"></iu-searchbox>
            <iu-button text="추가"></iu-button>
          </iu-toolbar>
        </iu-datatable>
      </v-flex>
    </v-layout>
    <!-- <iu-form :items="items">
      <small>*는 필수 입력입니다.</small>
      <v-spacer></v-spacer>
      <iu-button text="저장"></iu-button>
    </iu-form> -->
    <!-- <Layout></Layout> -->
    <!-- <Rio></Rio> -->
    <!-- <iu-button></iu-button> -->
    <!-- <iu-sub-header text="펼치기"></iu-sub-header> -->
    <!-- <div class="row-container">
      <p>hi</p>
      <p>world</p>
    </div> -->
  </v-container>
  <!-- </v-app> -->
</template>

<script>
import Rio from '@/projects/rio/Rio'
import Layout from '@/projects/example/layout'
import Types from '@/store/mutation-types'
import { mapActions } from 'vuex'

export default {
  name: 'HelloWorld',
  data() {
    return {
      search: '',
      headers: [
        {
          text: 'Dessert (100g serving)',
          align: 'left',
          sortable: false,
          value: 'name',
          render: (createElement, params) => {
            return createElement('h4', [
              createElement(
                'a',
                {
                  attrs: {
                    name: 'abc',
                    href: '#abc'
                  },
                  on: {
                    click: () => {
                      this.clickHandler(params.row)
                    }
                  }
                },
                params.column
              )
            ])
          }
        },
        { text: 'Calories', value: 'calories' },
        { text: 'Fat (g)', value: 'fat' },
        { text: 'Carbs (g)', value: 'carbs' },
        { text: 'Protein (g)', value: 'protein' },
        { text: 'Sodium (mg)', value: 'sodium' },
        { text: 'Calcium (%)', value: 'calcium' },
        { text: 'Iron (%)', value: 'iron' }
        // {
        //   sortable: false,
        //   render(createElement, params) {
        //     // return createElement('iu-button', {
        //     //       props: { text: '수정', classes: { 'ma-1': true, 'pa-0': true } }
        //     //     })
        //     return createElement('div', [
        //       createElement('iu-button', {
        //         props: { text: '수정', classes: { 'ma-1': true, 'pa-0': true } }
        //       }),
        //       createElement('iu-button', {
        //         props: { text: '삭제', classes: { 'ma-1': true, 'pa-0': true } }
        //       })
        //     ])
        //   }
        // }
        // {
        //   sortable: false,
        //   components: [
        //     {
        //       event: 'onDelete',
        //       icon: 'delete',
        //       text: '삭제',
        //       component: AmiButton
        //     },
        //     {
        //       event: 'onDelete',
        //       icon: 'update',
        //       text: '수정',
        //       component: AmiButton
        //     }
        //   ]
        // }
      ],
      records: [
        {
          value: false,
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          sodium: 87,
          calcium: '14%',
          iron: '1%'
        },
        {
          value: false,
          name: 'Ice cream sandwich',
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          sodium: 129,
          calcium: '8%',
          iron: '1%'
        },
        {
          value: false,
          name: 'Eclair',
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          sodium: 337,
          calcium: '6%',
          iron: '7%'
        },
        {
          value: false,
          name: 'Cupcake',
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          sodium: 413,
          calcium: '3%',
          iron: '8%'
        },
        {
          value: false,
          name: 'Gingerbread',
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          sodium: 327,
          calcium: '7%',
          iron: '16%'
        },
        {
          value: false,
          name: 'Jelly bean',
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          sodium: 50,
          calcium: '0%',
          iron: '0%'
        },
        {
          value: false,
          name: 'Lollipop',
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          sodium: 38,
          calcium: '0%',
          iron: '2%'
        },
        {
          value: false,
          name: 'Honeycomb',
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          sodium: 562,
          calcium: '0%',
          iron: '45%'
        },
        {
          value: false,
          name: 'Donut',
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          sodium: 326,
          calcium: '2%',
          iron: '22%'
        },
        {
          value: false,
          name: 'KitKat',
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          sodium: 54,
          calcium: '12%',
          iron: '6%'
        }
      ],
      items: [
        {
          members: [
            { type: 'textfield', label: '이름', model: '', field: 'name' },
            { type: 'textfield', label: '학교', model: '', field: 'school' },
            { type: 'textfield', label: '집주소', model: '', field: 'address' }
          ]
        },
        {
          members: [
            { type: 'textfield', label: '집주소', model: '', field: 'address' }
          ]
        },
        {
          members: [
            {
              type: 'textfield',
              label: '학교주소',
              model: '',
              field: 'school-address'
            }
          ]
        }
      ]
    }
  },
  components: {
    Rio,
    Layout
  },
  methods: {
    onSave() {
      console.log(this.items)
    },
    ...mapActions({
      getDoctorMembers: Types.GET_DOCTOR_MEMBERS
    }),
    clickHandler(row) {
      console.log(row)
    }
  },
  mounted() {
    // this.getDoctorMembers().then(response => console.log(response))
  }
}
</script>


<style>
.row-container {
  display: flex;
  flex-flow: row;
}
</style>
