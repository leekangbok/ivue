<template>
  <v-layout row
    wrap>
    <v-flex d-flex
      xs12
      sm3>
      <slot name="left"></slot>
    </v-flex>
    <v-flex d-flex
      xs12
      sm9>
      <v-layout row
        wrap>
        <v-flex d-flex
          xs12>
          <slot name="col1"></slot>
        </v-flex>
        <v-flex d-flex
          xs12>
          <slot name="col2"></slot>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>
