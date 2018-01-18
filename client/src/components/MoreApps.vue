<template>
  <v-menu origin="center center"
    transition="scale-transition"
    open-on-hover
    bottom
    left>
    <v-btn icon
      slot="activator">
      <v-icon>apps</v-icon>
    </v-btn>
    <v-list>
      <v-list-tile @click="">
        <v-list-tile-title>menu1</v-list-tile-title>
      </v-list-tile>
      <v-list-tile @click="">
        <v-list-tile-title>menu2</v-list-tile-title>
      </v-list-tile>
    </v-list>
  </v-menu>
</template>
