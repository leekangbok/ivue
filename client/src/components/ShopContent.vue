<template>
  <v-container fluid>
    <v-layout row
      wrap>
      <v-flex xs12
        sm2>
        <v-navigation-drawer permanent
          light
          :mini-variant.sync="mini">
          <v-list dense>
            <v-list-tile>
              <v-list-tile-action>
                <v-btn icon
                  @click.native.stop="mini = !mini">
                  <v-icon color="indigo">view_list</v-icon>
                </v-btn>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>CATEGORY</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-divider></v-divider>
            <v-list-tile @click="">
              <v-list-tile-action>
                <v-icon color="indigo">phone</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>핸드폰</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile @click="">
              <v-list-tile-action>
                <v-icon color="indigo">book</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>책</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-divider inset></v-divider>
            <v-list-tile @click="">
              <v-list-tile-action>
                <v-icon color="indigo">computer</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>컴퓨터</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile @click="">
              <v-list-tile-action>
                <v-icon color="indigo">build</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>도구</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-divider inset></v-divider>
            <v-list-tile @click="">
              <v-list-tile-action>
                <v-icon color="indigo">location_on</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>찾아오는길</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-navigation-drawer>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      mini: false
    }
  }
}
</script>
<style>
.media {
  height: 100%;
  margin: 0;
}
</style>
