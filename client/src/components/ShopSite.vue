<template>
  <!-- <iu-panel flat
        slot="link"
        color="transparent"> -->
    <v-layout justify-center>
      <v-flex xs6>
      <v-card flat color="transparent">
          <v-card-actions>
            <v-switch label="전체" v-model="selected" value="all"></v-switch>
            <v-switch label="이덴트" v-model="selected" value="edent"></v-switch>
            <v-switch label="K덴탈" v-model="selected" value="kdental"></v-switch>
          </v-card-actions>
        </v-card>
      </v-flex>
      <!-- <v-card-actions>
    <v-btn dark color="primary" @click="$store.commit('setSite')">전체보기</v-btn>
    <span>|</span>
    <v-btn dark color="primary" @click="$store.commit('setSite', 'edent')">이덴트</v-btn>
            <span>|</span>
    <v-btn dark color="primary" @click="$store.commit('setSite', 'kdental')">K덴탈</v-btn>
      </v-card-actions> -->
    </v-layout>
  <!-- </iu-panel> -->
</template>

<script>
export default {
  data() {
    return {
      selected: ['all']
    }
  },
  watch: {
    selected() {
      // if (this.selected.findIndex(x => x === 'all') >= 0) {
      //   this.selected = ['all']
      // }
      // if (this.selected.findIndex(x => x !== 'all') >= 0) {
      //   this.selected = this.selected.filter(x => x !== 'all')
      // }
      // if (this.selected.length === 0) {
      //   this.selected = ['all']
      // }
      this.$store.commit('setSite', this.selected)
    }
  }
}
</script>
