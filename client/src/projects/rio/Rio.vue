<template>
  <v-container fluid>
    <v-container>
      <iu-box1xcol2 class="align-center">
        <v-card flat
          slot="left">
          <v-card-media src="src/assets/서울봄빛치과-로고최종-1030x316.png"
            contain
            height="150">
          </v-card-media>
        </v-card>
        <v-card light
          flat
          slot="col1">
          <v-card-title primary-title>
            <h3 class="title mb-0 primary--text text--accent-4">
              <strong>환자가 추천하는 치과</strong>
            </h3>
          </v-card-title>
        </v-card>
        <iu-tabs :items="items"
          :expand="true"
          :slider="{color:'orange'}"
          @onEvent="tabChanged"
          slot="col2"
          activeClass="orange lighten-4"></iu-tabs>
      </iu-box1xcol2>
    </v-container>
    <section>
      <RioHeader v-bind="{backImg: 'src/assets/a.jpg', backHeight: 900}"></RioHeader>
    </section>
    <section>
      <RioBody></RioBody>
    </section>
    <section>
      <RioFooter></RioFooter>
    </section>
  </v-container>
</template>

<script>
import RioHeader from './rio-header'
import RioBody from './rio-body'
import RioFooter from './rio-footer'

export default {
  data() {
    return {
      items: [
        { text: '병원소개' },
        { text: '임플란트' },
        { text: '심미치료' },
        { text: '일반치료' },
        { text: '상담및예약' }
      ]
    }
  },
  methods: {
    tabChanged(item, id) {
      console.log(id)
    }
  },
  components: {
    RioHeader,
    RioBody,
    RioFooter
  }
}
</script>

<style>
.content {
  background-color: white;
}
</style>
