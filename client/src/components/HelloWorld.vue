<template>
  <v-app>
      <iu-form :items="items" @onSave="onSave"></iu-form>
  </v-app>
  <!-- <Layout></Layout> -->
  <!-- <Rio></Rio> -->
  <!-- <iu-button></iu-button> -->
  <!-- <iu-sub-header text="펼치기"></iu-sub-header> -->
</template>

<script>
import Rio from '@/projects/rio/Rio'
import Layout from '@/projects/example/layout'

export default {
  name: 'HelloWorld',
  data() {
    return {
      items: [
        {
          members: [
            { type: 'textfield', label: '이름', model: '', field: 'name' },
            { type: 'textfield', label: '학교', model: '', field: 'school' },
            { type: 'textfield', label: '집주소', model: '', field: 'address' }
          ]
        },
        {
          members: [{ type: 'textfield', label: '집주소', model: '', field: 'address' }]
        },
        {
          members: [{ type: 'textfield', label: '학교주소', model: '', field: 'school-address' }]
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
    }
  }
}
</script>