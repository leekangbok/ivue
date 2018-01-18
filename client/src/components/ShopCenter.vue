<template>
  <v-toolbar>
    <div class="d-flex align-center"
      style="margin-right: 10px;padding-left: 13%">
      <span>Logo</span>
    </div>
    <div class="d-flex align-center">
      <v-text-field prepend-icon="search"
            :prepend-icon-cb="() => $emit('onSearch', search)"
            @keyup.enter="$emit('onSearch', search)"
            v-model.trim="search"
            solo
            :append-icon="search ? 'clear' : ''"
            :append-icon-cb="() => search = ''"
            hide-details
            light
            single-line
            style="min-width: 600px"></v-text-field>
    </div>
    <div class="d-flex align-center"
      style="margin-left: auto;padding-right: 13%">
        <v-btn icon>
    <v-badge top
      color="green">
      <span slot="badge">6</span>
      <v-icon>shopping_cart</v-icon>
    </v-badge>
  </v-btn>
      <v-btn round flat outline>
        <v-icon left>perm_identity</v-icon>MyShop
      </v-btn>
    </div>
  </v-toolbar>
</template>

<script>
export default {
  data() {
    return {
      search: ''
    }
  }
}
</script>
