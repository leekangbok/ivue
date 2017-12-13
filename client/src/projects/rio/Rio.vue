<template>
  <v-app>
    <v-card flat
      fluid
      app>
      <v-layout row
        wrap>
        <v-flex d-flex
          xs12
          sm3
          md3>
          <v-card flat>
            <v-card-media src="http://www.bombit.co.kr/wp_bombitwin/wp-content/uploads/2015/09/%EC%84%9C%EC%9A%B8%EB%B4%84%EB%B9%9B%EC%B9%98%EA%B3%BC-%EB%A1%9C%EA%B3%A0%EC%B5%9C%EC%A2%85-1030x316.png"
              contain
              height="150">
            </v-card-media>
          </v-card>
        </v-flex>
        <v-flex d-flex
          xs12
          sm9
          md9>
          <v-layout row
            wrap>
            <v-flex d-flex
              xs12>
              <v-card light
                flat>
                <v-card-title primary-title>
                  <div>
                    <h3 class="title mb-0 indigo--text text--accent-4">
                      태어나서 첫 치과. 자연치아를 소중히 하는 치과. 안녕하세요. 리오치과 입니다.
                    </h3>
                  </div>
                </v-card-title>
              </v-card>
            </v-flex>
            <v-flex d-flex
              xs12>
              <!-- <v-card dark
                  color="green">
                  <v-card-text>11</v-card-text>
                </v-card> -->
              <v-tabs grow>
                <v-tabs-bar>
                  <v-tabs-slider color="orange"></v-tabs-slider>
                  <v-tabs-item active-class="grey lighten-4"
                    class="primary--text"
                    ripple
                    v-for="(item, i) in items"
                    :key="i"
                    :href="'#tab-' + (i + 1)">
                    {{ item }}
                  </v-tabs-item>
                </v-tabs-bar>
              </v-tabs>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-card>
    <v-content>
      <v-container fluid>
        <h1>컨텐츠</h1>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      items: ['병원소개', '임플란트', '심미치료', '일반치료', '상담및예약'],
      text:
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
    }
  }
}
</script>

<style>
.content {
  background-color: white;
}
</style>
