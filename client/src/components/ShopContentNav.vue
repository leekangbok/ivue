<template>
<v-card>
  <v-navigation-drawer permanent id="shop-nav-drawer">
      <v-list dense>
        <v-list-tile>
          <v-list-tile-action>
            <v-icon color="indigo">view_list</v-icon>
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
</v-card>
</template>

<script>
export default {
  data() {
    return {
      mini: false
    }
  },
  watch: {
    // '$vuetify.breakpoint'() {
    //   if (this.$vuetify.breakpoint.smAndDown) {
    //     this.mini = true
    //   } else {
    //     this.mini = false
    //   }
    // }
  },
  created() {
    // if (this.$vuetify.breakpoint.smAndDown) {
    //   this.mini = true
    // }
  }
}
</script>

<style scoped>
.navigation-drawer {
  width: auto !important;
  padding: 0px !important;
}
</style>
