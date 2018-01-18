<template>
  <v-layout row class="mt-4">
    <v-flex xs6 sm3>
      <v-card>
        <v-list dense subheader>
          <v-subheader inset>CATEGORY</v-subheader>
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
      </v-card>
    </v-flex>
  </v-layout>
</template>

<style>
.media {
  height: 100%;
  margin: 0;
}
</style>
