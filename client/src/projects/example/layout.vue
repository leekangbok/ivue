<template>
  <v-app>
    <v-toolbar height="150"
      app>
      <v-container>
        <v-layout row
          wrap
          align-end>
          <v-flex xs3
            class="hidden-xs-only">
            <v-card dark
              color="primary"
              height="100">
              <v-card-text>2</v-card-text>
            </v-card>
          </v-flex>
          <v-flex xs9>
            <v-card dark
              color="secondary">
              <v-card-text>10</v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-toolbar>
    <v-content>
      <h1>Rio</h1>
    </v-content>
  </v-app>
</template>

<style>
/* .content {
  background-color: white;
} */
</style>
