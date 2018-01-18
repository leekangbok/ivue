<template>
  <v-layout>
    <v-flex xs12
      sm6
      offset-sm3>
      <v-card>
        <v-card-media class="white--text"
          height="350px"
          src="/static/ver-economic-code-bitcoin-cash-story.jpg">
          <v-container fill-height
            fluid>
            <v-layout fill-height>
              <v-flex xs12
                align-end
                flexbox>
                <span class="headline">A new age is coming</span>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-media>
        <v-card-title>
          <div>
            <span class="grey--text">암호화폐</span><br>
            <span>비트코인</span><br>
            <span>이더리움, 리플...</span>
          </div>
        </v-card-title>
        <v-card-actions>
          <iu-button text="Explore"
            flat
            @onEvent="doMore"></iu-button>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  methods: {
    doMore() {}
  }
}
</script>
