<template>
  <iu-panel flat
        slot="link"
        color="transparent">
    <v-layout justify-center>
      <v-card-actions>
    <v-btn dark color="primary" @click="$store.commit('setSite')">전체보기</v-btn>
    <span>|</span>
    <v-btn dark color="primary" @click="$store.commit('setSite', 'edent')">이덴트</v-btn>
            <span>|</span>
    <v-btn dark color="primary" @click="$store.commit('setSite', 'kdental')">K덴탈</v-btn>
      </v-card-actions>
    </v-layout>
  </iu-panel>
</template>

<script>
export default {
  data() {
    return {}
  }
}
</script>
